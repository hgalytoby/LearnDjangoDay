from django.test import TestCase


# Create your tests here.

class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    result = []

    def listOfLeftLeaves(self, root, type=None):
        array = root.__dict__
        print(array)
        if array['left'] is not None:
            self.listOfLeftLeaves(array['left'], type='left')
        if array['right'] is not None:
            self.listOfLeftLeaves(array['right'], type='right')
        if array['left'] is None and type == 'left':
            self.result.append(array['val'])
        return self.result


if __name__ == '__main__':
    # root = Node(3)
    # # print(root.__dict__)
    # root.left = Node(9)
    # root.right = Node(20)
    # root.right.left = Node(15)
    # root.right.right = Node(7)
    # root.right.right.left = Node(11)
    # root.right.left.left = Node(666)
    # sol = Solution()
    # print(sol.listOfLeftLeaves(root))
    a = None
    if not a:
        print('in')
