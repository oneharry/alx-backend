#!/usr/bin/env python3
"""BasicCache Module"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BaseCache implementation """

    def __init__(self):
        """Initialize """
        super().__init__()

    def put(self, key, item):
        """ put item value into key key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value of key in cache"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
