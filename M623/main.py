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
    
class Solution(object):
    def addOneRow(self, root, val, depth):
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        
        queue = deque([(root, 1)])
        while queue:
            node, currentDepth = queue.popleft()
            if currentDepth == depth - 1:
                leftNode = TreeNode(val)
                leftNode.left = node.left
                node.left = leftNode
                
                rightNode = TreeNode(val)
                rightNode.right = node.right
                node.right = rightNode
            else:
                if node.left:
                    queue.append((node.left, currentDepth + 1))
                if node.right:
                    queue.append((node.right, currentDepth + 1))
        return root
        

solution = Solution()

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)

val = 1
depth = 3
newRoot = solution.addOneRow(root, val, depth)
printTree(newRoot)