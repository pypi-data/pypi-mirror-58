#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by pat on 9/1/19
"""
This module contains parsing utilities for US addresses.

.. currentmodule:: brnl_usaddress.parsing
.. moduleauthor:: Pat Daburu <pat@daburu.net>
"""
from functools import lru_cache
from typing import Mapping
from CaseInsensitiveDict import CaseInsensitiveDict
from bnrml import Normalizer
import usaddress
from .normalizers import by_component

MAX_PARSE_CACHE: int = 1024  #: the maximum number of parse results to cache


class UsAddressParser:
    """
    Parse US addresses.
    """
    def __init__(
            self,
            normalizers: Mapping[str, Normalizer] = None,
            auto_normalizers: bool = True,
            debug: bool = False
    ):
        """

        :param normalizers: the preferred normalizers
        :param auto_normalizers: `True` to load normalizers from configuration
            automatically
        :param debug: provide debugging information with results
        """
        self._normalizers = (
            dict(normalizers) if normalizers else {}
        )
        self._auto_normalizers: bool = auto_normalizers
        self._debug = debug

    @lru_cache(maxsize=MAX_PARSE_CACHE)
    def parse(self, address: str) -> Mapping[str, str]:
        """
        Parse a US address string.

        :param address: the address string
        :return: the parsed address
        """
        # Let's start by letting `usaddress` do it's thing.  We'll put the
        # result into a case-insensitive dictionary.
        parsed = usaddress.parse(address)

        # Now create a case-insensitive dictionary into which we can collect
        # the tuples in the `uadaddress` parse.
        parsedd = {}
        # Now go through all the tuples...
        for value, key in parsed:
            try:
                # If we've seen this key before there should be a list
                # of constituent values waiting.
                parsedd[key].append(value)
            except KeyError:
                # Otherwise we'll create one.
                parsedd[key] = [value]

        # Now we'll concatenate all the values.
        parsedd = CaseInsensitiveDict({
            k: ' '.join(v) for k, v in parsedd.items()
        })

        # Create a dictionary to hold debugging information.
        debug_nzn = {}
        debug = {
            'usaddress': {
                'parse': parsed
            },
            'bnrml': {
                'normalizations': debug_nzn
            }
        }

        # Let's go through all the components and see which ones will need
        # to be normalized.
        for component, value in parsedd.items():
            try:
                normalizer = self._normalizers[component]
            except KeyError:
                # If we're not supposed to try to update the collection of
                # normalizers automatically...
                if not self._auto_normalizers:
                    # ...just move along.
                    continue
                # Let's see if we can get a configured normalizer for this
                # component.
                normalizer = by_component(component)
                # In any case, save this result for next time.
                self._normalizers[component] = normalizer
            # If we have a normalizer for this component...
            if normalizer:
                # ...attempt the normalization.
                normalization = normalizer.normalize(value)
                # If we got a normalization...
                if normalization is not None:
                    # ...update the dictionary with the normalized value.
                    parsedd[component] = normalization.normalized
                # Add the result to the debugging information.
                debug_nzn[component] = (
                    normalization.export()
                    if normalization
                    else None
                )

        # One last pass: Lowercase all the values.
        parsedd = {k: v.lower() if v else v for k, v in parsedd.items()}

        # If we're supplying debugging information...
        if self._debug:
            parsedd['__debug__'] = debug

        # Return the mapping.
        return parsedd
