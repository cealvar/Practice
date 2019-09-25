class Node:
    def __init__(self, data="", next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

    def __str__(self):
        output = "Data: " + str(self.data) + "; Next: "
        output += str(self.next.data) if self.next else "None"
        return output

class DLLNode:
    def __init__(self, data="", prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_prev(self):
        return self.prev

    def set_prev(self, prev_node):
        self.prev = prev_node

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

    def __str__(self):
        output = "Data: " + str(self.data) + "; Prev: "
        output += str(self.prev.data) if self.prev else "None"
        output += "; Next: "
        output += str(self.next.data) if self.next else "None"
        return output

class TreeNode:
    def __init__(self, data="", left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_left_node(self):
        return self.left

    def set_left_node(self, left_node):
        self.left = left_node

    def get_right_node(self):
        return self.right

    def set_right_node(self, right_node):
        self.right = right_node

    def __str__(self):
        output = "Current Node: " + str(self.data) + "; Left Child: "
        output += str(self.left.data) if self.left else "None"
        output += "; Right Child: "
        output += str(self.right.data) if self.right else "None"
        return output

def main():
    print("f")
    dln = DLLNode("b")
    print(dln)
    n = Node("c")
    print(n)

if __name__ == '__main__':
    main()
