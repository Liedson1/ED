from task import Task
class AVLTree:
    class Node:
        def __init__(self, key=None, value=None, height=1):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.height = height

    def __init__(self):
        self.root = None

    def get_max(self):
        if self.root is None:
            return None

        node = self.root
        while node.right is not None:
            node = node.right

        return node.value

    def insert(self, task):
        self.root = self._insert(self.root, task)

    def _insert(self, node, task):
        if node is None:
            return self.Node(key=task.priority, value=task)

        if task.priority < node.key:
            node.left = self._insert(node.left, task)
        else:
            node.right = self._insert(node.right, task)

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and task.priority < node.left.key:
            return self._rotate_right(node)

        if balance < -1 and task.priority > node.right.key:
            return self._rotate_left(node)

        if balance > 1 and task.priority > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and task.priority < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, node):
        r = node.right
        rl = r.left

        r.left = node
        node.right = rl

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        r.height = 1 + max(self._height(r.left), self._height(r.right))

        return r

    def _rotate_right(self, node):
        l = node.left
        lr = l.right

        l.right = node
        node.left = lr

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        l.height = 1 + max(self._height(l.left), self._height(l.right))

        return l

    def _height(self, node):
        if node is None:
            return 0

        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0

        return self._height(node.left) - self._height(node.right)

    def decrescente(self, node):
        if node is not None:
            self.decrescente(node.right)
            print(node.value.descricao, end=' ')
            self.decrescente(node.left)

