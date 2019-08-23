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
        output = "Data: " + self.data + "\nNext: "
        output += self.next.data if self.next else "null"
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
        output = "Current Node: " + self.data + "; Left Child: "
        output += self.left.data if self.left else "null"
        output += "; Right Child: "
        output += self.right.data if self.right else "null"
        return output

def main():
    print("f")

if __name__ == '__main__':
    main()
