class HashMap:
    def __init__(self, cap = 227):
        self.cap = cap
        self.mappings = [[] for i in range(cap)] #[[]] * cap creates the same reference for each index
        self.size = 0
    
    def hashcode(self, key):
        if key:
            return sum([ord(c) for c in key]) % self.cap
        return 0

    def contains_key(self, key):
        index = self.hashcode(key)
        for item in self.mappings[index]:
            if item[0] == key:
                return True
        return False
    
    def contains_value(self, value):
        for bucket in self.mappings:
            for item in bucket:
                if item[1] == value:
                    return True
        return False

    def put(self, key, value):
        index = self.hashcode(key)
        updated = False
        for item in self.mappings[index]:
            if item[0] == key:
                item[1] = value
                updated = True
        if not updated:
            self.mappings[index].append([key, value])
            self.size += 1
    
    def remove(self, key):
        index = self.hashcode(key)
        for item in self.mappings[index]:
            if item[0] == key:
                del_key = item[0]
                del_val = item[1]
                self.mappings[index].remove([del_key, del_val])
                self.size -= 1 
                return del_val
        return None
    
    def get(self, key):
        index = self.hashcode(key)
        for item in self.mappings[index]:
            if item[0] == key:
                return item[1]
        return None

    def entry_set(self):
        mappings = {}
        for bucket in self.mappings:
            for item in bucket:
                mappings[item[0]] = item[1]
        return mappings
    
    def key_set(self):
        key_set = set()
        for bucket in self.mappings:
            for item in bucket:
                key_set.add(item[0])
        return key_set
    
    def values(self):
        mappings = {}
        for bucket in self.mappings:
            for item in bucket:
                mappings[item[0]] = item[1]
        return mappings.values()

    def put_all(self, hashmap):
        mappings = hashmap.entry_set()
        for key in mappings:
            self.put(key, mappings[key])
    
    def is_empty(self):
        return self.size == 0
    
    def __len__(self):
        return self.size
    
    def clear(self):
        self.mappings = [[]]
        self.size = 0

    def __str__(self):
        return str(self.mappings)

def main():
    hashmap = HashMap(5)
    print(hashmap.contains_key(None))
    print(hashmap.contains_value(None))
    print(hashmap.remove("None"))
    print(hashmap.get("None"))
    print(hashmap.entry_set())
    print(hashmap.key_set())
    print(list(hashmap.values()))
    print(hashmap.is_empty())
    print(len(hashmap))
    print(hashmap, "\n")
    
    hashmap.put("foo", 1)
    hashmap.put("bar", 2)
    hashmap.put("baz", 3)
    hashmap.put("qux", 4)
    hashmap.put("foobar", 5)
    hashmap.put("foo", 100)
    hashmap.put(None, None)
    hashmap.put(None, None)
    print(hashmap)
    print(hashmap.is_empty())
    print(len(hashmap))
    print(hashmap.contains_key("None"))
    print(hashmap.contains_value("None"))
    print(hashmap.remove("None"))
    print(hashmap.get("None"))
    print(hashmap.entry_set())
    print(hashmap.key_set())
    print(list(hashmap.values()), "\n")

    hashmap.remove(None)
    print(hashmap)
    print(hashmap.is_empty())
    print(len(hashmap))
    print(hashmap.contains_key("bar"))
    print(hashmap.contains_value(2))
    print(hashmap.get("bar"))
    print(hashmap.entry_set())
    print(hashmap.key_set())
    print(list(hashmap.values()), "\n")

    hashmap2 = HashMap(10)
    hashmap2.put("foo", 1)
    hashmap2.put("bar", 2)
    hashmap2.put("baz", 3)
    hashmap2.put("None", -100)
    hashmap2.put("oof", 500)
    hashmap2.put("rab", 600)
    hashmap2.put("hello world", 99)
    print(hashmap2)
    hashmap.put_all(hashmap2)
    print(hashmap)
    print(len(hashmap), "\n")
    
    hashmap.remove("foo")
    hashmap.remove("bar")
    hashmap.remove("baz")
    hashmap.remove("qux")
    hashmap.remove("foobar")
    hashmap.remove("None")
    hashmap.remove("oof")
    hashmap.remove("rab")
    hashmap.remove("hello world")
    print(hashmap)
    print(len(hashmap), "\n")

    hashmap2.clear()
    print(hashmap2)
    print(len(hashmap2))
    print(hashmap2.is_empty())

if __name__ == '__main__':
    main()