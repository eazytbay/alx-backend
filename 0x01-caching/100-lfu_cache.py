#!/usr/bin/env python3
""" create BaseCaching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system
    """

    def __init__(self):
        """
        Initialization of the class with the parent's init method
        """
        super().__init__()
        self.usage = []
        self.frequency = {}

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key is None or item is None:
            pass
        else:
            x = len(self.cache_data)
            if x >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                lfu = min(self.frequency.values())
                lfu_keys = []
                for y, z in self.frequency.items():
                    if z == lfu:
                        lfu_keys.append(y)
                if len(lfu_keys) > 1:
                    lru_lfu = {}
                    for y in lfu_keys:
                        lru_lfu[y] = self.usage.index(y)
                    discard = min(lru_lfu.values())
                    discard = self.usage[discard]
                else:
                    discard = lfu_keys[0]

                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.usage[self.usage.index(discard)]
                del self.frequency[discard]
            # update usage frequency
            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value linked to a given key, or None
        """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
