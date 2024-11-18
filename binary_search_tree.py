class Node():
    """
    Reference: https://gingerkang.tistory.com/86
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree():
    def __init__(self, root):
        self.root = root
    def insert(self, value):
        self.cur_node = self.root
        while True:
            if value < self.cur_node.value:
                if self.cur_node.left == None:
                    self.cur_node.left = Node(value)
                    break
                else:
                    self.cur_node = self.cur_node.left
            else:
                if self.cur_node.right == None:
                    self.cur_node.right = Node(value)
                    break
                else:
                    self.cur_node = self.cur_node.right


if __name__ == "__main__":
    root = Node(1)
    bst = BinarySearchTree(root)
