#!/usr/bin/python3
"""
2-lifo_cache.py

This module implements a basic LIFO caching system.

Author: Malik Hussein
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Caching class
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Add an item to the cache (LIFO Algorithm).
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        number_of_items = len(self.cache_data)

        if number_of_items > BaseCaching.MAX_ITEMS:
            if self.last_key:
                self.cache_data.pop(self.last_key)
                print(f'DISCARD: {self.last_key}')

        self.last_key = key

    def get(self, key):
        """
        Get an item by key.
        """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
