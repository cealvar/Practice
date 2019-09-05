from Node import Node

class QueueArray:
    def __init__(self):
        self.queue = []
        self.size = 0
    
    def add(self, item):
        self.queue.append(item)
        self.size += 1
    
    def remove(self):
        if self.size:
            item = self.queue[0]
            self.queue = self.queue[1:]
            self.size -= 1
            return item
        return None

    def peek(self):
        if self.size:
            return self.queue[0]
        return None
    
    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.queue)

class QueueList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, item):
        new_node = Node(item)
        if self.last:
            self.last.set_next(new_node)
        self.last = new_node
        if not self.first:
            self.first = new_node
        self.size += 1

    def remove(self):
        item = self.last
        if self.first:
            self.first = self.first.get_next()
            if not self.first:
                self.last = None
            self.size -= 1
            return item.get_data()
        return None
    
    def is_empty(self):
        return self.size == 0
    def peek(self):
        if self.size:
            return self.first.get_data()
        return None
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        curr = self.first
        out = "["
        while curr:
            out += str(curr.get_data())
            if curr.get_next():
                out += ", "
            curr = curr.get_next()
        out += "]"
        return out

def main():
    print("Queue implemented using an array...")
    queue = QueueArray()
    queue.add(1)
    queue.remove()
    queue.remove()
    queue.remove()
    print(queue)
    print(len(queue))
    print(queue.is_empty())
    print(queue.peek())
    queue.add(1)
    queue.add(2)
    queue.add(3)
    print(queue)
    print(len(queue))
    print(queue.is_empty())
    print(queue.peek())
    queue.remove()
    print(queue)
    print(len(queue))
    print(queue.is_empty())
    print(queue.peek())
    queue.remove()
    print(queue)
    print(len(queue))
    print(queue.is_empty())
    print(queue.peek())
    queue.remove()
    print(queue)
    print(len(queue))
    print(queue.is_empty())
    print(queue.peek())

    print("\nQueue implemented using a linked list...")
    queue = QueueList()
    queue.add(1)
    queue.remove()
    queue.remove()
    queue.remove()
    print(queue)
    print(len(queue))
    print(queue.is_empty())
    print(queue.peek())
    queue.add(1)
    queue.add(2)
    queue.add(3)
    print(queue)
    print(len(queue))
    print(queue.is_empty())
    print(queue.peek())
    queue.remove()
    print(queue)
    print(len(queue))
    print(queue.is_empty())
    print(queue.peek())
    queue.remove()
    print(queue)
    print(len(queue))
    print(queue.is_empty())
    print(queue.peek())
    queue.remove()
    print(queue)
    print(len(queue))
    print(queue.is_empty())
    print(queue.peek())

if __name__ == '__main__':
    main()