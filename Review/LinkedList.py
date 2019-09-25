from Node import Node
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, new_data):
        new_node = Node(new_data)
        new_node.set_next(self.head)
        if not self.head:
            self.tail = new_node
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head:
            self.tail.set_next(new_node)
        else:
            self.head = new_node
        self.tail = new_node

    def add_kth_pos(self, pos, new_data):
        new_node = Node(new_data)
        if self.head:
            if pos == 1:
                new_node.set_next(self.head)
                self.head = new_node
            else:
                trailer = self.head
                curr = self.head.get_next()
                curr_pos = 2
                while curr and curr_pos <= pos:
                    if curr_pos == pos:
                        new_node.set_next(curr)
                        trailer.set_next(new_node)
                    trailer = trailer.get_next()
                    curr = curr.get_next()
                    curr_pos += 1
                if curr_pos == pos:
                    trailer.set_next(new_node)
                    self.tail = new_node             
        else:
            if pos == 1:
                self.head, self.tail = new_node, new_node

    def remove_first(self):
        first = self.head
        if first:
            self.head = first.get_next()
            if not self.head:
                self.tail = None
        return first

    def remove_last(self):
        removed = self.tail
        if self.head and self.head.get_next():
            second_last = self.head
            last = self.head.get_next()
            while last.next:
                second_last = second_last.get_next()
                last = second_last.get_next()
            second_last.set_next(None)
            self.tail = second_last
            return last
        self.head = None
        self.tail = None
        return removed

    def remove_kth_pos(self, pos):
        if self.head and pos == 1:
            removed = self.head
            self.head = self.head.get_next()
            if not self.head:
                self.tail = self.head
            return removed
        if self.head and self.head.get_next():
            trailer = self.head
            curr = self.head.get_next()
            curr_pos = 2
            while curr and curr_pos <= pos:
                if curr_pos == pos:
                    trailer.set_next(curr.get_next())
                    if not trailer.get_next():
                        self.tail = trailer
                    return curr
                trailer = trailer.get_next()
                curr = curr.get_next()
                curr_pos += 1
        return None

    def search(self, data):
        curr = self.head
        while curr:
            if curr.get_data() == data:
                return curr
            curr = curr.get_next()
        return None

    def clear(self):
        self.head = None
        self.tail = None

    def __len__(self):
        ''' return lenght of the list '''
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
                curr_pos += 1
    
    def __delitem__(self, key):
        ''' delete item at key index '''
        if isinstance(key, int):
            if self.head and key == 0:
                self.head = self.head.get_next()
                if not self.head:
                    self.tail = self.head
            elif self.head and self.head.get_next():
                trailer = self.head
                curr = self.head.get_next()
                curr_pos = 1
                while curr and curr_pos <= key:
                    if curr_pos == key:
                        trailer.set_next(curr.get_next())
                        if not trailer.get_next():
                            self.tail = trailer
                    trailer = trailer.get_next()
                    curr = curr.get_next()
                    curr_pos += 1

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
            if curr.get_next():
                out += ", "
            curr = curr.get_next()
        out += "]"
        return out
    
def main():
    l = LinkedList()
    l.add_first("a")
    l.append("b")
    l.clear()
    print("Tail: " + str(l.tail))
    print("Head: " + str(l.head))
    print(l)
    l.append("c")
    l.add_first("d")
    print(l)
    l.clear()
    l.add_kth_pos(0,"A")
    l.add_kth_pos(2, "a")
    print(l)
    l.remove_first()
    l.remove_last()
    l.remove_kth_pos(0)
    l.remove_kth_pos(1)
    del l[0]
    del l[1]
    print(l)
    l.add_kth_pos(1, "a")
    print(l)
    l.remove_kth_pos(1)
    print(l)
    l.append(1)
    l.add_kth_pos(2, 2)
    l.add_kth_pos(3, 3)
    l.add_kth_pos(1, 4)
    l.add_kth_pos(4, 5)
    print("Tail: " + str(l.tail))
    print("Head: " + str(l.head))
    print(l)
    l.add_kth_pos(6, 6)
    l.add_kth_pos(8, 10)
    print("Tail: " + str(l.tail))
    print("Head: " + str(l.head))
    print(l)
    l.remove_kth_pos(1)
    l.remove_kth_pos(5)
    l.remove_kth_pos(5)
    l.remove_kth_pos(2)
    print("Tail: " + str(l.tail))
    print("Head: " + str(l.head))
    print(l)
    print(l.search(1))
    print(l.search(5))
    print(l.search(3))
    print(l[-1])
    print(l[0])
    print(l[1])
    print(l[2])
    print(l[3])
    l[-1] = "z"
    l[0] = "a"
    l[1] = "b"
    l[2] = "c"
    l[3] = "d"
    print("Tail: " + str(l.tail))
    print("Head: " + str(l.head))
    print(l)
    print("deleting l[0]")
    del l[0]
    print("Tail: " + str(l.tail))
    print("Head: " + str(l.head))
    print("deleting l[1]")
    del l[1]
    print("Tail: " + str(l.tail))
    print("Head: " + str(l.head))
    print("deleting l[0]")
    del l[0]
    print("Tail: " + str(l.tail))
    print("Head: " + str(l.head))
    print(l)
    del l[0]
    print(l)
    print(len(l))
    print(1 in l)
    print("A" in l)
    for i in l:
        print("item: " + i)
    l.append(1)
    l.append(3)
    l.append(5)
    l.append(9)
    l.append(-100)
    print(-100 in l)
    print(1 in l)
    for i in l:
        print("item: " + str(i))
    print("Tail: " + str(l.tail))
    print("Head: " + str(l.head))
    print(l)
    reversed(l)
    print("Tail: " + str(l.tail))
    print("Head: " + str(l.head))
    print(l)
    print(len(l))
    

if __name__ == '__main__':
    main()