from Node import *
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, new_data):
        new_node = Node(new_data)
        if self.head:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head:
            self.tail.set_next(new_node)
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def add_kth_pos(self, pos, new_data):
        new_node = Node(new_data)
        trailer = self.head
        curr_pos = 2
        while trailer and curr_pos <= pos:
            curr = trailer.get_next()
            if curr_pos == pos:
                trailer.set_next(new_node)
                new_node.set_next(curr)
                if not curr:
                    self.tail = new_node
            if curr:
                curr = curr.get_next()
            trailer = trailer.get_next()
            curr_pos += 1
        if pos == 1:
            if self.head:
                new_node.set_next(self.head)
                self.head = new_node
            else:
                self.head = new_node
                self.tail = new_node

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

    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.get_next()
        return count

    def __getitem__(self, key):
        ''' search element at index position '''
        if isinstance(key, int):
            curr = self.head
            count = 0
            while curr and count <= key:
                if count == key:
                    return curr.get_data()
                curr = curr.get_next()
                count += 1
        return None
    
    def __setitem__(self, key, value):
        ''' replace item at key with value '''
        if isinstance(key, int):
            curr = self.head
            curr_pos = 0
            while curr and curr_pos <= key:
                if curr_pos == key:
                    curr.set_data(value)
                curr = curr.get_next()
                curr += 1
    
    def __delitem__(self, key):
        ''' delete item at key index '''
        if isinstance(key, int):
            trailer = self.head
            curr_pos = 1
            while trailer and curr_pos <= key:
                curr = trailer.get_next()
                if curr_pos == key and curr:
                    nxt = curr.get_next()
                    trailer.set_next(nxt)
                    if not nxt:
                        self.tail = trailer
                trailer = trailer.get_next()
                curr_pos += 1
            if key == 0 and self.head:
                self.head = self.head.get_next()

    def __iter__(self):
        ''' returns iterator object representation of linked list '''
        curr = self.head
        item_array = []
        while curr:
            item_array.append(curr.get_data())
            curr = curr.get_next()
        return iter(item_array)
    
    def __reversed__(self):
        ''' reverses linked list '''
        self.tail = self.head
        prev = None
        curr = self.head
        nxt = None
        while curr:
            nxt = curr.get_next()
            curr.set_next(prev)
            prev = curr
            curr = nxt
        self.head = prev
    
    def __contains__(self, item):
        ''' implementation of membership test operators '''
        curr = self.head
        while curr:
            if curr.get_data() == item:
                return True
            curr = curr.get_next()
        return False
    
    def __str__(self):
        ''' computes lrintable string represntation of linked list '''
        curr = self.head
        out = "["
        while curr:
            out += str(curr.get_data())
            print(curr.get_data())
            if curr.get_next():
                out += ", "
            curr = curr.get_next()
        out += "]"
        return out
    
def main2():
    print("dd")
    l = LinkedList()
    l.add_kth_pos(1,"a")
    l.add_kth_pos(2, "b")
    l.add_kth_pos(3, None)
    print(None in l)

if __name__ == '__main__':
    main2()