"""To create a basic dictionary"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class implementing a simple dictionary"""

    def __init__(self):
        """The constructor method"""
        super().__init__()

    def put(self, key, item):
        """a method that add items to the dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """returns the value of the data linked to the key"""
        if key:
            if key in self.cache_data.keys():
                return self.cache_data[key]
        return None
