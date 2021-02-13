import collections

class LRUCache:

    def __init__(self, capacity):
        if capacity >= 0:
            self.LRU = collections.OrderedDict()
            self.capacity = capacity
        
    def get(self, key)
        if key in self.LRU.keys():
            self.LRU.move_to_end(key)
            return self.LRU[key]
        return -1

    def put(self, key, value)
        if key in self.LRU.keys():
            self.LRU[key] = value
            self.LRU.move_to_end(key)
        else:
            if len(self.LRU.keys()) == self.capacity:
                self.LRU.popitem(last=False)
            self.LRU[key] = value
