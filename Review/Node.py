class Node:
    def __init__(self, data="", next=None):
        self.data = data
        self.next = next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, next_node):
        self.next = next_node

    def __str__(self):
        output = "Data: " + self.data + "\nNext: "
        if self.next:
            output += self.next.data
        else:
            output += "null"
        return output

def main():
    n = Node("a")
    print(n)
    print(n.data)
    print(n.next)
    n.setNext(Node("b", None))
    print(n.next.data)
    n.setData("c")
    print(n.data)
    n.data = "dds"
    print(n.data)
    print(n)

if __name__ == '__main__':
    main()
