#!/usr/bin/env python3
"""Module - 2-lifo_cache.py"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching and implements
        a LIFO caching system
    """
    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.order.pop(-2)
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
