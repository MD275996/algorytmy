class TreeNode:

    def __init__(self, value, left_child=None, right_child=None):
        self.value = value              # string, stored value
        self.left_child = left_child    # None or TreeNode instance
        self.right_child = right_child  # None or TreeNode instance

    def get_value(self):
        return self.value

    def add_left_child(self, value):
        pass

    def add_right_child(self, value):
        pass

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def has_left_child(self) -> bool:
        if self.left_child != None:
            return True
        else:
            return False

    def has_right_child(self) -> bool:
        if self.right_child != None:
            return True
        else:
            return False

    def is_leaf(self) -> bool:
        if self.has_left_child() or self.has_right_child():
            return False
        else:
            return True

    def __str__(self):
        pieces = []
        self._parenthesize_recur(pieces)
        return ''.join(pieces)
    
    def _parenthesize_recur(self, result):
        if self.is_leaf():
            if self.value == None:
                print(self.value)
            else:
                result.append(str(self.value))
        else:
            result.append("(")
            if self.has_left_child():
                self.left_child._parenthesize_recur(result)
            result.append(str(self.value))
            if self.has_right_child():
                self.right_child._parenthesize_recur(result)
            result.append(")")


# treeNode1 = TreeNode(1)
# treeNode2 = TreeNode(2)
# treeNode3 = TreeNode("+",treeNode1,treeNode2)

# treeNode4 = TreeNode("-",treeNode1,treeNode2)
# treeNode = TreeNode("*",treeNode3,treeNode4)

# print(treeNode)
