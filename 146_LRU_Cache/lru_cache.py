class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.__capactiy = capacity
        self.__cache = [None for _ in range(0, self.__capactiy)]

    @property
    def cache(self):
        return self.__cache

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for idx in range(0, self.__capactiy):
            e = self.__cache[idx]
            if e is None:
                return -1
            k, v = e
            if k == key:
                self.__cache[0], self.__cache[idx] = self.__cache[idx], self.__cache[0]
                return v
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        for idx in range(0, self.__capactiy):
            e = self.__cache[idx]
            if e is None:
                continue
            k, v = e
            if k == key:
                print('here')
                self.__cache[idx] = (key, value)
                self.__cache[0], self.__cache[idx] = self.__cache[idx], self.__cache[0]
                return

        # entry not exist already, add it to the first None spot.
        for idx in range(0, self.__capactiy):
            e = self.__cache[idx]
            if e is None:
                print('here', key, value)
                self.__cache[idx] = (key, value)
                self.__cache[0], self.__cache[idx] = self.__cache[idx], self.__cache[0]
                return

        # else override the least recently used element
        self.__cache[-1] = (key, value)
        self.__cache[0], self.__cache[-1] = self.__cache[-1], self.__cache[0]


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
# param_1 = obj.get(key)
# obj.put(key,value)
# ["", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [,   [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
print(obj.cache)
print(obj.put(1, 1))
print(obj.cache)
print(obj.put(2, 2))
print(obj.cache)
print(obj.get(2))
print(obj.cache)
print(obj.get(1))
print(obj.cache)
print(obj.put(3, 3))
print(obj.cache)
print(obj.get(2))
print(obj.cache)
print(obj.put(4, 4))
print(obj.cache)
print(obj.get(1))
print(obj.cache)
print(obj.get(3))
print(obj.cache)
print(obj.get(4))
print(obj.cache)
