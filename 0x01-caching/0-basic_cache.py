class BaseCaching:
    """Base class for caching systems"""
    cache_data = {}  # Shared dictionary for storing cached data

class BasicCache(BaseCaching):
    """Basic caching system with no limit"""

    def put(self, key, item):
        """
        Stores an item value in the cache for a given key.

        Args:
            key (str): The key to associate the item with.
            item (object): The item to store in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the item value associated with a given key from the cache.

        Args:
            key (str): The key to search for.

        Returns:
            object: The value associated with the key, or None if not found.
        """
        if key is not None:
            return self.cache_data.get(key) 

