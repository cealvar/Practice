from LinkedList import LinkedList

class HashTable:
    def __init__(self, size = 227):
        self.size = size
        self.mappings = [None] * size

    def contains_key(self, key, index):
        for item in self.mappings[index]:
            if item[0] == key:
                return True
        return False
    
    def contains_value(self, value, index):
        for item in self.mappings[index]:
            if item[1] == value:
                return True
        return False
    
    def hashcode(self, key):
        return sum([ord(c) for c in key]) % self.size
    
    def put(self, key, value):
        index = self.hashcode(key)
        if self.mappings[index]:
            updated = False
            for item in self.mappings[index]:
                if item[0] == key:
                    item[1] = value
                    updated = True
            if not updated:
                self.mappings[index].append([key, value])
        else:
            self.mappings[index] = [[key, value]]

    def get(self, key):
        index = self.hashcode(key)
        if self.mappings[index]:
            for item in self.mappings[index]:
                if item[0] == key:
                    return item[1]
        return None
    

        