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
        if self.head:
            self.head = first.get_next()
        return first

    def remove_last(self):
        end = self.tail
        if self.head:
            curr = self.head
            while curr.get_next():
                if curr.get_next == self.tail:
                    self.tail = curr
        return end
    
    def __str__(self):
        curr = self.head
        out = ""
        while curr:
            print("dsdssd")
            if curr.get_data():
                out += str(curr.get_data()) + " -> "
            else:
                out += "null -> "
            curr = curr.get_next()
        out += "null"
        return out
    
def main2():
    l = LinkedList()
    l.add_kth_pos(0, Node("a", None))
    l.add_kth_pos(2, Node("b", None))
    print(l)
    print(" Adding 1")
    l.add_kth_pos(1, Node("a", None))
    print(" Adding 2")
    l.add_kth_pos(2, Node("b", None))
    print(" Adding 3")
    l.add_kth_pos(3, Node("c", None))
    l.add_kth_pos(5, Node("d", None))
    l.add_kth_pos(0, Node("e", None))
    l.add_kth_pos(5, Node("1", None))
    print(l)
    print("DONE")
    print(l.tail)

if __name__ == '__main__':
    main2()