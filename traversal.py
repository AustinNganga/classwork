class TreeNode:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value


    def insert(self,key):
        if key < self.value:
            if self.left is None:
                self.left = TreeNode(key)
            else:
                self.left.insert(key)

        elif key > self.value:
            if self.right is None:
                self.right = TreeNode(key)

            else:
                self.right.insert(key)



    def pre_order_traversal(self):
        print(self.value)
        if self.left:
            self.left.pre_order_traversal()


        if self.right:
            self.right.pre_order_traversal()


    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.value)

        if self.right:
            self.right.in_order_traversal()



    def post_order_traversal(self):

        if self.left:
            self.left.post_order_traversal()

        if self.right:
            self.right.post_order_traversal()

        print(self.value)

    def find(self,key):
        if key < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(key)

        elif key > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(key)

        else:
            return True




if __name__ == '__main__':
    tree = TreeNode(10)
    tree.insert(5)
    tree.insert(3)
    tree.insert(4)
    tree.insert(11)

    tree.insert(12)
    tree.insert(13)

    print("This is pre order traversal")
    tree.pre_order_traversal()

    print("This is in order traversal")
    tree.in_order_traversal()

    print("This is post order traversal")
    tree.post_order_traversal()

