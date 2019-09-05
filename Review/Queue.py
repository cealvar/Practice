from Node import Node

class QueueArray:
    def __init__(self):
        self.queue = []
        self.size = 0
    
    def add(self, item):
        self.stack.append(item)
        self.size += 1
    
    def remove(self):
        if self.size:
            item = self.stack[self.size-1]
            self.stack = self.stack[:self.size-1]
            self.size -= 1
            return item
        return None

    def peek(self):
        if self.size:
            return self.stack[self.size-1]
        return None
    
    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.stack)