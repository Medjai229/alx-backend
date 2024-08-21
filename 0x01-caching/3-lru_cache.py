"""
3-lru_cache.py

This module implements a basic LRU caching system.

Author: Malik Hussein
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU Caching class
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.lru_arr = []

    def update_lru_arr(self, key):
        """
        Updates the Least Recently Used (LRU) array by removing
        the given key if it exists and appending it to the end.
        """
        if key:
            if key in self.lru_arr:
                self.lru_arr.remove(key)
            self.lru_arr.append(key)

    def put(self, key, item):
        """
        Add an item to the cache (LRU Algorithm).
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.update_lru_arr(key)

        number_of_items = len(self.cache_data)

        if number_of_items > BaseCaching.MAX_ITEMS:
            lru_key = self.lru_arr.pop(0)
            self.cache_data.pop(lru_key)
            print(f'DISCARD: {lru_key}')

    def get(self, key):
        """
        Get an item by key.
        """
        if key is None or key not in self.cache_data.keys():
            return None

        if key in self.lru_arr:
            self.update_lru_arr(key)

        return self.cache_data[key]
