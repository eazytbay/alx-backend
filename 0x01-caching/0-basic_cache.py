#!/usr/bin/env python3
""" create BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Definition of  a class for caching information in key-value pairs
    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """

    def __init__(self):
        """
        Initialization of  the class using the parent class __init__ method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Stores a key-value pair
        Args:
            Key
            Item
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return value linked to key.
        If key is None or doesn't exist, return None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
