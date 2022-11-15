import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        s = ''
        if (root != None):
            q = [root]
            while (len(q) != 0):
                s += str(q[0].data) + ' '
                if (q[0].left != None):
                    q.append(q[0].left)
                if (q[0].right != None):
                    q.append(q[0].right)
                q.pop(0)
        print (s)
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)