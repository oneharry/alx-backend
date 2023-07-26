#!/usr/bin/env python3
"""FIFOCache Module"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache implementation """

    def __init__(self):
        """Initialize """
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """ put item value into key key"""
        if key is None or item is None:
            return
        num_cachedata = len(self.cache_data)
        if num_cachedata >= BaseCaching.MAX_ITEMS:
            rm_key = self.queue.popleft()
            self.cache_data.pop(rm_key)
            print("DISCARD: {}".format(rm_key))
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """ Return the value of key in cache"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
