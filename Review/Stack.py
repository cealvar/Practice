from Node import *
class StackArray:
    def __init__(self):
        self.stack = []
        self.size = 0
    
    def push(self, item):
        self.stack.append(item)
        self.size += 1
    
    def pop(self):
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

class StackList:
    def __init__(self):
        self.head = None
        self.top = None
        self.size = 0
    
    def push(self, item):
        new_node = Node(item, self.top)
        self.top = new_node
        self.size += 1
    
    def pop(self):
        item = self.top.get_data()
        if self.top:
            self.top = self.top.get_next()
            self.size -= 1
        return item

    def peek(self):
        return self.top
    
    def is_empty(self):
        return not self.head

    def __len__(self):
        return self.size

    def __str__(self):
        curr = self.head
        out = "["
        while curr:
            out += str(curr.get_data())
            if curr.get_next():
                out += " ,"
            curr = curr.get_next()
        out += "]"
        return out

def main3():
    print("Stack implemented using an array...")
    stack = StackArray()
    stack.push(1)
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack)
    print(len(stack))
    print(stack.is_empty())
    print(stack.peek())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(len(stack))
    print(stack.is_empty())
    print(stack.peek())
    stack.pop()
    print(stack)
    print(len(stack))
    print(stack.is_empty())
    print(stack.peek())
    stack.pop()
    print(stack)
    print(len(stack))
    print(stack.is_empty())
    print(stack.peek())
    stack.pop()
    print(stack)
    print(len(stack))
    print(stack.is_empty())
    print(stack.peek())

    print("\nStack implemented using a linked list...")
    stack = StackArray()
    stack.push(1)
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack)
    print(len(stack))
    print(stack.is_empty())
    print(stack.peek())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(len(stack))
    print(stack.is_empty())
    print(stack.peek())
    stack.pop()
    print(stack)
    print(len(stack))
    print(stack.is_empty())
    print(stack.peek())
    stack.pop()
    print(stack)
    print(len(stack))
    print(stack.is_empty())
    print(stack.peek())
    stack.pop()
    print(stack)
    print(len(stack))
    print(stack.is_empty())
    print(stack.peek())
    
if __name__ == '__main__':
    main3()



