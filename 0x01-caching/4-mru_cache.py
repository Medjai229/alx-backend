"""
4-mru_cache.py

This module implements a basic MRU caching system.

Author: Malik Hussein
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRU Caching class
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.mru_arr = []

    def update_mru_arr(self, key):
        """
        Updates the Most Recently Used (MRU) array by removing
        the given key if it exists and appending it to the end.
        """
        if key:
            if key in self.mru_arr:
                self.mru_arr.remove(key)
            self.mru_arr.append(key)

    def put(self, key, item):
        """
        Add an item to the cache (MRU Algorithm).
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.update_mru_arr(key)

        number_of_items = len(self.cache_data)

        if number_of_items > BaseCaching.MAX_ITEMS:
            mru_key = self.mru_arr.pop(-2)
            self.cache_data.pop(mru_key)
            print(f'DISCARD: {mru_key}')

    def get(self, key):
        """
        Get an item by key.
        """
        if key is None or key not in self.cache_data.keys():
            return None

        if key in self.mru_arr:
            self.update_mru_arr(key)

        return self.cache_data[key]
