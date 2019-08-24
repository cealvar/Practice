from Node import *
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, node):
        if node:
            if self.head:
                node.set_next(self.head)
                self.head = node
            else:
                self.head = node
                self.tail = node

    def add_last(self, node):
        if self.head:
            self.tail.set_next(node)
            self.tail = node
        else:
            self.add_first(node)

    def add_kth_pos(self, pos, node):
        if node:
            trailer = self.head
            curr_pos = 2
            while trailer and curr_pos <= pos:
                curr = trailer.get_next()
                if curr_pos == pos:
                    trailer.set_next(node)
                    node.set_next(curr)
                    if not curr:
                        self.tail = node
                if curr:
                    curr = curr.get_next()
                trailer = trailer.get_next()
                curr_pos += 1
            if pos == 1:
                if self.head:
                    node.set_next(self.head)
                    self.head = node
                else:
                    self.head = node
                    self.tail = node

    def remove_first(self):
        first = self.head
        if first:
            self.head = first.get_next()
        return first

    def remove_last(self):
        removed = self.tail
        if self.head:
            curr = self.head
            nxt = curr.get_next()
            while nxt:
                if nxt == self.tail:
                    curr.set_next(None)
                    self.tail = curr
                    removed = nxt
                curr = curr.get_next()
                nxt = nxt.get_next()
            if curr == self.head:
                self.head = None
                self.tail = None
        return removed

    def remove_kth_pos(self, pos):
        removed = None
        trailer = self.head
        curr_pos = 2
        while trailer and curr_pos <= pos:
            curr = trailer.get_next()
            if curr_pos == pos and curr:
                nxt = curr.get_next()
                trailer.set_next(nxt)
                removed = curr
                if not nxt:
                    self.tail = trailer
            trailer = trailer.get_next()
            curr_pos += 1
        if pos == 1 and self.head:
            removed = self.head
            self.head = self.head.get_next()
        return removed

    def search(self, data):
        curr = self.head
        while curr:
            if curr.get_data() == data:
                return curr
            curr = curr.get_next()
        return None

    def __getitem__(self, key):
        ''' search element at index position '''
        curr = self.head
        count = 0
        while curr and isinstance(key, int) and count <= key:
            if count == key:
                return curr
            curr = curr.get_next()
            count += 1
        return None
    
    def __setitem__(self, key, value):
        ''' replace item at key with value '''
        print(key, value)
        if value and isinstance(key, int):
            curr = self.head
            curr_pos = 0
            while curr and curr_pos <= key:
                if curr_pos == key:
                    curr.set_data(value)
                curr = curr.get_next()
                curr_pos += 1
    
    def __delitem__(self, key):
        if self.head and isinstance(key, int):
            trailer = self.head
            curr = trailer.get_next()
            curr_pos = 1
            while trailer and curr_pos <= key:
                if curr_pos == 
    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.get_next()
        return count
    
    def __str__(self):
        curr = self.head
        out = ""
        while curr:
            if curr.get_data():
                out += str(curr.get_data()) + " -> "
            else:
                out += "null -> "
            curr = curr.get_next()
        out += "null"
        return out
    
def main2():
    l = LinkedList()
    l.add_kth_pos(1, Node("a", None))
    #print("Adding 2")
    l.add_kth_pos(2, Node("b", None))
    #print("Adding 3")
    l.add_kth_pos(3, Node("c", None))
    print(l['a'])
    l[-1] = "ss"
    print(l)

if __name__ == '__main__':
    main2()