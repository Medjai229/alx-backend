"""
100-lfu_cache.py

This module implements a basic LFU caching system.

Author: Malik Hussein
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU Caching class
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.lfu_freq = {}
        self.lru_arr = []

    def put(self, key, item):
        """
        Add an item to the cache (LFU Algorithm).
        """
        if key is None or item is None:
            return

        if key in self.cache_data.keys():
            # If the key is already in the cache,
            # update the value and increment the frequency.
            self.cache_data[key] = item
            self.lfu_freq[key] += 1
            # Remove the key from the LRU array and add it to the end.
            self.lru_arr.remove(key)
            self.lru_arr.append(key)

        else:
            # If the cache is at capacity,
            # discard the least frequently used item.
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the minimum frequency.
                min_freq = min(self.lfu_freq.values())

                # Find all keys with the minimum frequency.
                keys_with_min_freq = [
                    k for k, freq in self.lfu_freq.items() if freq == min_freq
                    ]

                # If there are multiple keys with the same frequency,
                # find the one that was most recently added.
                if len(keys_with_min_freq) > 1:
                    for k in self.lru_arr:
                        if k in keys_with_min_freq:
                            lru_key = k
                            break

                else:
                    lru_key = keys_with_min_freq[0]

                # Discard the least recently used item.
                self.cache_data.pop(lru_key)
                self.lfu_freq.pop(lru_key)
                self.lru_arr.remove(lru_key)
                print(f"DISCARD: {lru_key}")

            # Add the new item to the cache.
            self.cache_data[key] = item
            self.lfu_freq[key] = 1
            self.lru_arr.append(key)

    def get(self, key):
        """
        Get an item by key.
        """
        if key is None or key not in self.cache_data.keys():
            return None

        self.lfu_freq[key] += 1
        self.lru_arr.remove(key)
        self.lru_arr.append(key)

        return self.cache_data[key]
