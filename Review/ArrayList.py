from Node import *
class LinkedList:
    def __init__(self):
        self.list = []
        self.head = None
        self.tail = None

    def add_first(self, new_data):
        self.list = [new_data] + self.list
        self.head, self.tail = self.list[0], self.list[-1]

    def append(self, new_data):
        self.list.append(new_data)

    def add_kth_pos(self, pos, new_data):
        if pos > 0 and pos <= len(self.list):
            left = self.list[:pos-1]
            right = self.list[pos-1:]
            self.list = left + [new_data] + right

    def remove_first(self):
        self.list = self.list[1:]
        self.head, self.tail = self.list[0], self.list[-1]

    def remove_last(self):
        self.list[:-1]
        self.head, self.tail = self.list[0], self.list[-1]

    def remove_kth_pos(self, pos):
        if pos > 0 and pos <= len(self.list):
            left = self.list[:pos-1]
            right = self.list[pos:]
            self.list = left + right
            self.head, self.tail = self.list[0], self.list[-1]

    def search(self, data):
        for item in self.list:
            if data == item.get_data():
                return item
        return None

    def clear(self):
        self.list, self.head, self.tail = [], None, None

    def __len__(self):
        ''' return lenght of the list '''
        return len(self.list)

    def __getitem__(self, key):
        ''' search element at index position '''
    
    def __setitem__(self, key, value):
        ''' replace item at key with value '''
    
    def __delitem__(self, key):
        ''' delete item at key index '''

    def __iter__(self):
        ''' returns iterator object representation of linked list '''
    
    def __reversed__(self):
        ''' reverses linked list '''
    
    def __contains__(self, item):
        ''' implementation of membership test operators '''
    
    def __str__(self):
        ''' computes lrintable string represntation of linked list '''
    
def main2():
    l = LinkedList()
    '''
    l.add_first("a")
    l.append("b")
    print(l)
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
    del l[0]
    print("Tail: " + str(l.tail))
    print("Head: " + str(l.head))
    del l[1]
    print("Tail: " + str(l.tail))
    print("Head: " + str(l.head))
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
    '''
    

if __name__ == '__main__':
    main3()