#!/usr/bin/env python3
"""create Base Dictionary
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Definition of a Basic Caching system
    """
    def __init__(self):
        """Initialization of the BasicCache instance"""
        super().__init__()

    def put(self, key, item):
        """Assginment of value to the self.cache_key dictionary
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieval of the key-value from the self.cache_data dict
        """
        value = self.cache_data.get(key)
        return value
