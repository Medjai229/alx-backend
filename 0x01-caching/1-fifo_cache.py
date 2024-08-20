#!/usr/bin/python3
"""
1-fifo_cache.py

This module implements a basic FIFO caching system.

Author: Malik Hussein
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Caching class
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache (FIFO Algorithm).
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        number_of_items = len(self.cache_data)

        if number_of_items > BaseCaching.MAX_ITEMS:
            first_key, _ = next(iter(self.cache_data.items()))
            self.cache_data.pop(first_key)
            print(f'DISCARD: {first_key}')

    def get(self, key):
        """
        Get an item by key.
        """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
