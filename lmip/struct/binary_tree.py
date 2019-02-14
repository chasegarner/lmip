class BinaryTree:

    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def insert(self, insert_value):
        if self._root is None:
            self._root = _BinaryTreeNode(insert_value)
        else:
            self._root.insert(insert_value)

    def search(self, search_value):
        if self._root is None:
            return None
        else:
            return self._root.search(search_value)

    def to_list(self):
        if self._root is None:
            return []
        return self._root.to_list()


class _BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def has_two_children(self):
        return self.left is not None and self.right is not None

    def has_no_children(self):
        return self.left is None and self.right is None

    def insert(self, insert_value):
        if insert_value <= self.value:
            if self.left is None:
                self.left = _BinaryTreeNode(insert_value)
            else:
                self.left.insert(insert_value)
        else:
            if self.right is None:
                self.right = _BinaryTreeNode(insert_value)
            else:
                self.right.insert(insert_value)

    def search(self, search_value):
        if search_value == self.value:
            return self
        elif search_value <= self.value:
            return None if self.left is None else self.left.search(search_value)
        else:
            return None if self.right is None else self.right.search(search_value)

    def to_list(self):  # This is an "in-order" traversal
        if self.value is None:
            return []
        elif self.left is not None and self.right is not None:
            return self.left.to_list() + [self.value] + self.right.to_list()
        elif self.left is not None:
            return self.left.to_list() + [self.value]
        elif self.right is not None:
            return [self.value] + self.right.to_list()
        else:
            return [self.value]


class NotFound(Exception):
    pass
