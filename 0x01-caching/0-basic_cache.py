#!/usr/bin/env python3
""" To create a BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Definition of  a class for caching information in key-value pairs
    Methods:
        put(key, item) - this stores a key-value pair
        get(key) - this retrieves the value associated with a key
    """

    def __init__(self):
        """
        Initialization the class using the parent class __init__ method
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
        Returns the value linked to key.
        If key is None or does not exist, return None or do nothing
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
