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
            if self.head.get_next() == self.head:
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
        if curr:
            if curr.get_data() == data:
                return curr
            curr = curr.get_next()
            while curr != self.head:
                if curr.get_data() == data:
                    return curr
                curr = curr.get_next()
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
        while curr.get_next() != self.head:
            curr = curr.get_next()
            count += 1
        return count

    def __getitem__(self, key):
        ''' search element at index position '''
        if isinstance(key, int) and self.head:
            curr = self.head
            if key == 0:
                return curr
            curr = curr.get_next()
            count = 1
            while curr != self.head:
                if count == key:
                    return curr.get_data()
                curr = curr.get_next()
                count += 1
        return None
    
    def __setitem__(self, key, value):
        ''' replace item at key with value '''
        if isinstance(key, int) and self.head:
            curr = self.head
            if key == 0:
                curr.set_data(value)
            else:
                curr = curr.get_next()
                curr_pos = 1
                while curr != self.head:
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
        ''' computes Printable string represntation of linked list '''
        curr = self.head
        out = "["
        size = len(self)
        count = 0
        while curr and count < size:
            out += "Index " + str(count) + " -> " + "CURR: " + str(curr.get_data()) + "; PREV: " + str(curr.get_prev().get_data()) + "; NXT: " + str(curr.get_next().get_data()) + "\n"
            curr = curr.get_next()
            count += 1
        out += "]"
        return out

def main():
    
    print(".....................DOUBLY LINKED LIST.................................")
    dl = DoublyLinkedList()
    print(dl)
    print("\nadding z................")
    dl.add_kth_pos(2, "z")
    print(dl)
    print(dl.head)
    print(dl.tail)
    print("\nadding a................")
    dl.add_kth_pos(1, "A")
    print(dl)
    print(dl.head)
    print(dl.tail)
    print("\nadding b..................")
    dl.add_kth_pos(2, "b")
    print(dl)
    print(dl.head)
    print(dl.tail)
    print("\nadding c..................")
    dl.add_kth_pos(2, "c")
    print(dl)
    print(dl.head)
    print(dl.tail)
    print("\nadding d..................")
    dl.add_kth_pos(1, "d")
    print(dl)
    print(dl.head)
    print(dl.tail)
    print("\nadding e..................")
    dl.add_kth_pos(4, "e")
    print(dl)
    print(dl.head)
    print(dl.tail)
    print("\nadding f..................")
    dl.add_kth_pos(7, "e")
    print(dl)
    print(dl.head)
    print(dl.tail)
    print("\nadding f..................")
    dl.add_kth_pos(3, "f")
    print(dl)
    print(dl.head)
    print(dl.tail)
    


    print("\nremoving at position -1................")
    dl.remove_kth_pos(-1)
    print(dl)
    print(dl.head)
    print(dl.tail)
    print("\nremoving at position 7................")
    dl.remove_kth_pos(7)
    print(dl)
    print(dl.head)
    print(dl.tail)
    print("\nremoving at position 1................")
    dl.remove_kth_pos(1)
    print(dl)
    print(dl.head)
    print(dl.tail)
    print("\nremoving at position 3................")
    dl.remove_kth_pos(3)
    print(dl)
    print(dl.head)
    print(dl.tail)
    print("\nremoving at position 4................")
    dl.remove_kth_pos(4)
    print(dl)
    print(dl.head)
    print(dl.tail)
    print("\nremoving at position 2................")
    dl.remove_kth_pos(2)
    print(dl)
    print(dl.head)
    print(dl.tail)
    print("\nremoving at position 2................")
    dl.remove_kth_pos(2)
    print(dl)
    print(dl.head)
    print(dl.tail)
    print("\nremoving at position 1................")
    dl.remove_kth_pos(1)
    print(dl)
    print(dl.head)
    print(dl.tail)

if __name__ == '__main__':
    main()