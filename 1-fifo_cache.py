#!/usr/bin/env python3

"""
caching model(fifo)
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """caching algorithm(fifo)"""

    def __init__(self):
        """using the init method to initialize fifocaching"""
        super().__init__()

    def put(self, key, item):
        """ creates a method that adds items to the cache_data dict"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                first_element = next(iter(self.cache_data))
                self.cache_data.pop(first_element)
                print("DISCARD: {}".format(first_element))
        if key in self.cache_data:
            pass
        else:
            self.cache_data[key] = item
        return self.cache_data

    def get(self, key):
        """ get key values from cached data"""
        if key is None or key not in self.cached_data:
            return None
        return self.cached_data.get(key)
