#!/usr/bin/env python3
"""LRUCache Module"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ FIFOCache implementation """

    def __init__(self):
        """Initialize """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ put item value into key key"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
            self.queue.remove(key)
        else:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                rm_key = self.queue.pop(0)
                self.cache_data.pop(rm_key)
                print("DISCARD: {}".format(rm_key))

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """ Return the value of key in cache"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
