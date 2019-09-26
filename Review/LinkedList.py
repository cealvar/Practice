from Node import Node, DLLNode
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

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, new_data):
        new_node = DLLNode(new_data)
        if self.head:
            new_node.set_prev(self.tail)
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.tail.set_next(new_node)
        else:
            new_node.set_prev(new_node)
            new_node.set_next(new_node)
            self.tail = new_node
        self.head = new_node

    def append(self, new_data):
        new_node = DLLNode(new_data)
        if self.head:
            new_node.set_prev(self.tail)
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.tail.set_next(new_node)
        else:
            new_node.set_prev(new_node)
            new_node.set_next(new_node)
            self.head = new_node
        self.tail = new_node

    def add_kth_pos(self, pos, new_data):
        new_node = DLLNode(new_data)
        new_node.set_prev(new_node)
        new_node.set_next(new_node)
        if self.head:
            size = len(self)
            if pos > 0 and pos <= size + 1:
                curr = self.head
                curr_pos = 1
                while curr_pos < pos:
                    curr = curr.get_next()
                    curr_pos += 1
                prev = curr.get_prev()
                prev.set_next(new_node)
                curr.set_prev(new_node)
                new_node.set_prev(prev)
                new_node.set_next(curr)
                if pos == 1:
                    self.head = new_node
                elif pos == size + 1:
                    self.tail = new_node    
        else:
            if pos == 1:
                self.head, self.tail = new_node, new_node

    def remove_first(self):
        first = self.head
        if first:
            if first.get_next() == first:
                self.head, self.tail = None, None
            else:
                self.head = self.head.get_next()
                self.head.set_prev(self.tail)
                self.tail.set_next(self.head)
        return first

    def remove_last(self):
        removed = self.tail
        if self.head:
            if removed.get_next() == removed:
                self.head, self.tail = None, None
            else:
                self.tail = self.tail.get_prev()
                self.tail.set_next(self.head)
                self.head.set_prev(self.tail)
        return removed

    def remove_kth_pos(self, pos):
        if self.head:
            if self.head.get_next() == self.head and pos == 1:
                removed = self.head
                self.head, self.tail = None, None
                return removed
            size = len(self)
            if pos > 0 and pos <= size:
                curr = self.head
                curr_pos = 1
                while curr_pos < pos:
                    curr = curr.get_next()
                    curr_pos += 1
                prev = curr.get_prev()
                nxt = curr.get_next()
                prev.set_next(nxt)
                nxt.set_prev(prev)
                if pos == 1:
                    self.head = nxt
                if pos == size:
                    self.tail = prev
                return curr
        return None

    def search(self, data):
        curr = self.head
        while curr != self.tail:
            if curr.get_data() == data:
                return curr
            curr = curr.get_next()
        if curr and curr.get_data() == data:
            return curr
        return None

    def clear(self):
        self.head = None
        self.tail = None

    def __len__(self):
        ''' return lenght of the list '''
        if not self.head:
            return 0
        count = 1
        curr = self.head
        while curr != self.tail:
            curr = curr.get_next()
            count += 1
        return count

    def __getitem__(self, key):
        ''' search element at index position '''
        if isinstance(key, int) and self.head:
            curr = self.head
            curr_index = 0
            while curr != self.tail:
                if curr_index == key:
                    return curr.get_data()
                curr = curr.get_next()
                curr_index += 1
            if curr_index == key:
                return curr.get_data()
        return None
    
    def __setitem__(self, key, value):
        ''' replace item at key with value '''
        if isinstance(key, int) and self.head:
            curr = self.head
            curr_index = 0
            while curr != self.tail:
                if curr_index == key:
                    curr.set_data(value)
                curr = curr.get_next()
                curr_index += 1
            if curr_index == key:
                curr.set_data(value)
    
    def __delitem__(self, key):
        ''' delete item at key index '''
        if isinstance(key, int) and self.head:
            if self.head == self.head.get_next() and key == 0:
                self.head = None
                self.tail = None
            else:
                size = len(self)
                if key >= 0 and key < size:
                    curr = self.head
                    curr_index = 0
                    while curr_index < key:
                        curr = curr.get_next()
                        curr_index += 1
                    prev = curr.get_prev()
                    nxt = curr.get_next()
                    prev.set_next(nxt)
                    nxt.set_prev(prev)
                    if key == 0:
                        self.head = nxt
                    if key == size - 1:
                        self.tail = prev

    def __iter__(self):
        ''' returns iterator object representation of linked list '''
        curr = self.head
        item_array = []
        if curr:
            item_array.append(curr.get_data())
            curr = curr.get_next()
            while curr != self.head:
                item_array.append(curr.get_data())
                curr = curr.get_next()
        return iter(item_array)
    
    def __reversed__(self):
        ''' reverses DLL '''
        if self.head:
            prev = self.tail
            curr = self.head
            nxt = self.head.get_next()
            while curr != self.tail:
                curr.set_prev(nxt)
                curr.set_next(prev)
                prev = curr
                curr = nxt
                nxt = nxt.get_next()
            curr.set_prev(nxt)
            curr.set_next(prev)
            self.head, self.tail = self.tail, self.head
    
    def __contains__(self, item):
        ''' implementation of membership test operators '''
        curr = self.head
        while curr != self.tail:
            if curr.get_data() == item:
                return True
            curr = curr.get_next()
        if curr and curr.get_data() == item:
            return True
        return False
    
    def __str__(self):
        ''' computes Printable string represntation of linked list '''
        curr = self.head
        out = "["
        size = len(self)
        count = 0
        while count < size:
            out += "Index " + str(count) + " -> " + "CURR: " + str(curr.get_data()) + "; PREV: " + str(curr.get_prev().get_data()) + "; NXT: " + str(curr.get_next().get_data())
            curr = curr.get_next()
            count += 1
            if count != size:
                out += "\n"
        out += "]"
        return out

def main():
    print(".........................SINGLY LINKED LIST.........................")
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
    


    print("\n\n\n\n\n.........................DOUBLY LINKED LIST.........................")
    print("\nTesting Empty Lists..........")
    dl = DoublyLinkedList()
    print(dl)
    dl.remove_first()
    dl.remove_last()
    dl.remove_kth_pos(0)
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Searching for 'a':", dl.search("a"))
    print("Size of DLL:", len(dl))
    print("Getting item at index 0:", dl[0])
    dl[0] = "a"
    print("Setting item at index 0 to 'a'...")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Removing item at index 0...")
    dl.remove_kth_pos(0)
    print(dl)
    print("Deleting item at index 0...")
    del dl[0]
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Beginning FOR loop...")
    for i in dl:
        print(i)
    print("Ending FOR loop...")
    print("Reversing DLL...")
    reversed(dl)
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Checking if DLL contains 'a':", "a" in dl)
    print("Clearing DLL")
    dl.clear()
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)

    print("\n\nTesting SINGLE element Lists..........")
    print("\nAdding 'a' to beginning of DLL...")
    dl.add_first("a")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at beginning of DLL...")
    dl.remove_first()
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    
    print("\nAppending 'a' to DLL...")
    dl.append("a")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at end of DLL...")
    dl.remove_last()
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)

    print("\nAdding 'a' to beginning of DLL...")
    dl.add_first("a")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Removing item at position 2 of DLL...")
    dl.remove_kth_pos(2)
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Removing item at position 1 of DLL...")
    dl.remove_kth_pos(1)
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)

    print("\nAdding 'a' at position 1 of DLL...")
    dl.add_kth_pos(1 ,"a")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at index 1 of DLL...")
    del dl[1]
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Removing item at index 0 of DLL...")
    del dl[0]
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)

    print("\nAdding 'a' to beginning of DLL...")
    dl.add_first("a")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Searching for 'a':", dl.search("a"))
    print("Searching for 'b':", dl.search("b"))
    print("Size of DLL:", len(dl))
    print("Getting item at index 0:", dl[0])
    print("Getting item at index 1:", dl[1])
    print("Setting item at index 1 to 'c'...")
    dl[0] = "b"
    print("Setting item at index 0 to 'b'...")
    dl[0] = "b"
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Beginning FOR loop...")
    for i in dl:
        print(i)
    print("Ending FOR loop...")
    print("Reversing DLL...")
    reversed(dl)
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Checking if DLL contains 'a':", "a" in dl)
    print("Checking if DLL contains 'b':", "b" in dl)
    print("Clearing DLL")
    dl.clear()
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)

    print("\n\nTesting DOUBLE element Lists..........")
    print("\nAdding 'a' to beginning of DLL...")
    dl.add_first("a")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Adding 'b' to beginning of DLL...")
    dl.add_first("b")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at beginning of DLL...")
    dl.remove_first()
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at beginning of DLL...")
    dl.remove_first()
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)

    print("\nAppending 'a' to DLL...")
    dl.append("a")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Appending 'b' to DLL...")
    dl.append("b")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at end of DLL...")
    dl.remove_last()
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at end of DLL...")
    dl.remove_last()
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)

    print("\nAdding 'a' to beginning of DLL...")
    dl.add_first("a")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Appending 'b' to DLL...")
    dl.append("b")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Removing item at position -1 of DLL...")
    dl.remove_kth_pos(-1)
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Removing item at position 3 of DLL...")
    dl.remove_kth_pos(3)
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Removing item at position 1 of DLL...")
    dl.remove_kth_pos(1)
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Removing item at position 1 of DLL...")
    dl.remove_kth_pos(1)
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)

    print("\nAppending 'a' to DLL...")
    dl.append("a")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Adding 'b' to beginning of DLL...")
    dl.add_first("b")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Removing item at position 2 of DLL...")
    dl.remove_kth_pos(2)
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Removing item at position 1 of DLL...")
    dl.remove_kth_pos(1)
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)

    print("\nAdding 'a' at position 1 of DLL...")
    dl.add_kth_pos(1 ,"a")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Adding 'b' at position 1 of DLL...")
    dl.add_kth_pos(1 ,"b")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at index -1 of DLL...")
    del dl[-1]
    print("Deleting item at index 2 of DLL...")
    del dl[2]
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at index 0 of DLL...")
    del dl[0]
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at index 0 of DLL...")
    del dl[0]
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)

    print("\nAdding 'a' at position 1 of DLL...")
    dl.add_kth_pos(1 ,"a")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Adding 'b' at position 2 of DLL...")
    dl.add_kth_pos(2 ,"b")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at index 1 of DLL...")
    del dl[1]
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at index 0 of DLL...")
    del dl[0]
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)

    print("\nAdding 'a' to beginning of DLL...")
    dl.add_first("a")
    print("Adding 'b' to beginning of DLL...")
    dl.add_first("b")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Searching for 'a':", dl.search("a"))
    print("Searching for 'b':", dl.search("b"))
    print("Searching for 'c':", dl.search("c"))
    print("Size of DLL:", len(dl))
    print("Getting item at index 0:", dl[0])
    print("Getting item at index 1:", dl[1])
    print("Getting item at index 2:", dl[2])
    print("Setting item at index 2 to 'c'...")
    dl[2] = "b"
    print("Setting item at index 0 to 'z'...")
    dl[0] = "z"
    print("Setting item at index 1 to 'x'...")
    dl[1] = "x"
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Beginning FOR loop...")
    for i in dl:
        print(i)
    print("Ending FOR loop...")
    print("Reversing DLL...")
    reversed(dl)
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Checking if DLL contains 'a':", "a" in dl)
    print("Checking if DLL contains 'x':", "x" in dl)
    print("Checking if DLL contains 'z':", "z" in dl)
    print("Clearing DLL")
    dl.clear()
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)


    print("\n\nTesting MANY element Lists..........")
    print("\nAdding 'a' to beginning of DLL...")
    dl.add_first("a")
    print("Adding 'b' to beginning of DLL...")
    dl.add_first("b")
    print("Adding 'c' to beginning of DLL...")
    dl.add_first("c")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at beginning of DLL...")
    dl.remove_first()
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at beginning of DLL...")
    dl.remove_first()
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at beginning of DLL...")
    dl.remove_first()
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)

    print("\nAppending 'a' to DLL...")
    dl.append("a")
    print("Appending 'b' to DLL...")
    dl.append("b")
    print("Appending 'c' to DLL...")
    dl.append("c")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at end of DLL...")
    dl.remove_last()
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at end of DLL...")
    dl.remove_last()
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at end of DLL...")
    dl.remove_last()
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)

    print("\nAdding 'a' to beginning of DLL...")
    dl.add_first("a")
    print("Appending 'b' to DLL...")
    dl.append("b")
    print("Adding 'c' to beginning of DLL...")
    dl.add_first("c")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Removing item at position -1 of DLL...")
    dl.remove_kth_pos(-1)
    print("Removing item at position 4 of DLL...")
    dl.remove_kth_pos(4)
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Removing item at position 2 of DLL...")
    dl.remove_kth_pos(2)
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Removing item at position 1 of DLL...")
    dl.remove_kth_pos(1)
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Removing item at position 1 of DLL...")
    dl.remove_kth_pos(1)
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)

    print("\nAdding 'a' at position 1 of DLL...")
    dl.add_kth_pos(1 ,"a")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Adding 'b' at position 1 of DLL...")
    dl.add_kth_pos(1 ,"b")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Adding 'z' at position 3 of DLL...")
    dl.add_kth_pos(3 ,"z")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Adding 'x' at position 2 of DLL...")
    dl.add_kth_pos(2 ,"x")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at index -1 of DLL...")
    del dl[-1]
    print("Deleting item at index 4 of DLL...")
    del dl[4]
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at index 2 of DLL...")
    del dl[2]
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at index 0 of DLL...")
    del dl[0]
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at index 1 of DLL...")
    del dl[1]
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Deleting item at index 0 of DLL...")
    del dl[0]
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)

    print("\nAppending 'a' to DLL...")
    dl.append("a")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Appending 'b' to DLL...")
    dl.append("b")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Appending 'c' to DLL...")
    dl.append("c")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Appending 'd' to DLL...")
    dl.append("d")
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Searching for 'a':", dl.search("a"))
    print("Searching for 'b':", dl.search("b"))
    print("Searching for 'c':", dl.search("c"))
    print("Searching for 'd':", dl.search("d"))
    print("Searching for 'e':", dl.search("e"))
    print("Size of DLL:", len(dl))
    print("Getting item at index 0:", dl[0])
    print("Getting item at index 1:", dl[1])
    print("Getting item at index 2:", dl[2])
    print("Getting item at index 3:", dl[3])
    print("Getting item at index 4:", dl[4])
    print("Setting item at index 0 to 'w'...")
    dl[0] = "w"
    print("Setting item at index 1 to 'x'...")
    dl[1] = "x"
    print("Setting item at index 2 to 'y'...")
    dl[2] = "y"
    print("Setting item at index 3 to 'z'...")
    dl[3] = "z"
    print("Setting item at index 4 to 'q'...")
    dl[4] = "q"
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Beginning FOR loop...")
    for i in dl:
        print(i)
    print("Ending FOR loop...")
    print("Reversing DLL...")
    reversed(dl)
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)
    print("Checking if DLL contains 'w':", "w" in dl)
    print("Checking if DLL contains 'x':", "x" in dl)
    print("Checking if DLL contains 'y':", "y" in dl)
    print("Checking if DLL contains 'z':", "z" in dl)
    print("Checking if DLL contains 'q':", "q" in dl)
    print("Clearing DLL")
    dl.clear()
    print(dl)
    print("Head:", dl.head)
    print("Tail:", dl.tail)

if __name__ == '__main__':
    main()