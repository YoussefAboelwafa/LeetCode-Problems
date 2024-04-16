from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printTree(root):
    if root is None:
        print("null")
        return

    queue = deque([root])
    while queue:
        # don't print if all nodes are None in the queue (last level of the tree)
        if all(node is None for node in queue):
            break

        node = queue.popleft()
        if node is None:
            print("null", end=",")
        else:
            print(node.val, end=",")
            queue.append(node.left)
            queue.append(node.right)
