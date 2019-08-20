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
        output += self.next.data if self.next else "null"
        return output

class TreeNode:
    def __init__(self, data="", left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def setData(self, new_data):
        self.data = new_data

    def setLeftNode(self, left_node):
        self.left = left_node

    def setRightNode(self, right_node):
        self.right = right_node

    def __str__(self):
        output = "Current Node: " + self.data + "; Left Child: "
        output += self.left.data if self.left else "null"
        output += "; Right Child: "
        output += self.right.data if self.right else "null"
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
    t = TreeNode("ddd")
    print(t)

if __name__ == '__main__':
    main()
