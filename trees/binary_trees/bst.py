class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add data to the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data to the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.in_order()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order()

        return elements

    def post_order(self):
        pass
    def pre_order(self):
        pass

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right.delete(val)
        else:
            if self.left is not None and self.right is not None:
                return None
            if self.left is None:
                return self.right

            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self 
    

# aux function
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root
        
if __name__ == '__main__':
    nums = [25, 5, 9, 56, 23, 2, 64, 36, 7, 46]
    nums_tree = build_tree(nums)
    print(nums_tree.in_order())