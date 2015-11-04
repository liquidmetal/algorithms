class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self._left = None
        self._right = None

    def set_value(self, value):
        self.value = value
        return

    def set_left(self, left):
        self._left = left
        return

    def set_right(self, right):
        self._right = right
        return

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

class BinaryTree(object):
    def __init__(self, root):
        self.root = root
        return

    def traversal_level_order(self):
        ret = ""
        to_visit = [self.root]

        while len(to_visit) > 0:
            dequeue = to_visit[0]
            to_visit.remove(dequeue)

            ret += dequeue.value

            l = dequeue.get_left()
            r = dequeue.get_right()

            if l:
                to_visit.append(l)

            if r:
                to_visit.append(r)

        return ret

    def traversal_inorder(self):
        ret = ""
        stack = []
        current = self.root

        done = False
        while not done:
            if current:
                stack.append(current)
                current = current._left
            else:
                if len(stack) > 0:
                    current = stack.pop()
                    ret += current.value
                    current = current._right
                else:
                    done = True

        return ret

    def leaf_count(self):
        def _recurse(root):
            if not root.get_left() and not root.get_right():
                return 1

            return _recurse(root.get_left()) + _recurse(root.get_right())

        return _recurse(self.root)

