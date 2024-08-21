class TreeNode:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data) -> None:
        # insert to root
        if self.data is None:
            self.data = data

        # insert to left node
        elif data < self.data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)

        # insert to right node
        elif data > self.data:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)

    def visualize(self) -> None:
        if self.left:
            self.left.visualize()

        print(self.data)

        if self.right:
            self.right.visualize()

    def in_order_traversal(self, root):
        iter: list = []
        if root:
            iter = self.in_order_traversal(root.left)
            iter.append(root.data)
            iter += self.in_order_traversal(root.right)
        return iter

    def pre_order_tranversal(self, root):
        iter: list = []
        if root:
            iter.append(root.data)
            iter += self.pre_order_tranversal(root.left)
            iter += self.pre_order_tranversal(root.right)
        return iter

    def post_order_tranversal(self, root):
        iter: list = []
        if root:
            iter = self.post_order_tranversal(root.left)
            iter += self.post_order_tranversal(root.right)
            iter.append(root.data)
        return iter


def main():
    root: TreeNode = TreeNode(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    root.visualize()
    print(root.in_order_traversal(root))
    print(root.pre_order_tranversal(root))
    print(root.post_order_tranversal(root))


if __name__ == '__main__':
    main()
