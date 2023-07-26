#!/usr/bin/env python3
"""LFUCache Module"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache implementation """

    def __init__(self):
        """Initialize """
        super().__init__()
        self.queue = []
        self.count = {}

    def __lfu(self, dic_keys):
        """returns the LRU if more than 1 item has LFU match"""
        for i in range(len(self.queue)):
            if self.queue[i] in dic_keys:
                return self.queue[i]

    def put(self, key, item):
        """ put item value into key key"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
            self.queue.remove(key)
            self.count[key] = self.count[key] + 1
        else:
            self.count[key] = 1
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                rm_key = min(self.queue, key=lambda x: (self.count[x],
                             self.queue.index(x)))

                self.cache_data.pop(rm_key)
                self.queue.remove(rm_key)
                print("DISCARD: {}".format(rm_key))

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """ Return the value of key in cache"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
