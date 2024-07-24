#!/usr/bin/env python3
"""Module - 100-lfu_cache.py"""

from base_caching import BaseCaching
from collections import OrderedDict, defaultdict


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching and implements
        a LFU caching system
    """
    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.cache_data = {}
        self.frequency = defaultdict(int)
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key = self.get_lfu_key()
                if lfu_key:
                    print(f"DISCARD: {lfu_key}")
                    del self.cache_data[lfu_key]
                    del self.frequency[lfu_key]
                    del self.usage_order[lfu_key]
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order[key] = None

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.usage_order.move_to_end(key)
        return self.cache_data[key]

    def get_lfu_key(self):
        """ Helper function to find the least frequently used key """
        if not self.frequency:
            return None

        min_freq = min(self.frequency.values())
        lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]
        if len(lfu_keys) == 1:
            return lfu_keys[0]

        # If there is more than one key with the same frequency, use LRU
        lfu_key = None
        for key in self.usage_order:
            if key in lfu_keys:
                lfu_key = key
                break
        return lfu_key
