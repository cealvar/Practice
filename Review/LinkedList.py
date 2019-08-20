from Review.Node import *
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = None

    def add_first(self, node):
        if not self.head:
            self.tail = node
        if node:
            node.set_next(self.head)
            self.head = node

    def add_last(self, node):
        if self.head:
            self.tail.set_next(node)
            self.tail = node
        else:
            self.add_first(node)

    def add_kth_pos(self, pos, node):
        if pos == 1:
            self.add_first(node)
        else:
            if pos > 1 and self.head:
                count = 2
                curr = self.head
                nxt = curr.get_next()
                while curr and count <= pos:
                    if count == pos:
                        curr.set_next(node)
                        node.set_next(nxt)
                        curr.set_next(node)
                    curr = curr.get_next()
                    nxt = nxt.get_next()

        if self.head:
            count = 0
            curr = self.head
            while curr:


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