#!/usr/bin/python3
"""
0-basic_cache.py

This module implements a basic cache which stores data in a dictionary.

Author: Malik Hussein
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Caching class
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key.
        """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
