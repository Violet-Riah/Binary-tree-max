class Node:
 def init_(self,data):
        self.data =data
        self.left =self.right= None
def findMax(root):
       if(root==None):
        return float('-inf')
       res = root.data
       lres = findMax(root.left)
       rres = findMax(root.right)
       if (lres > res):
        res = lres
       if (rres > res):
        res = rres
        return res
       if __name__ == '__main__':
         root = Node(3)
       root.left = Node(20)
       root.right = Node(8)
       root.left.right = Node(4)
       root.left.right.left = Node(2)
       root.left.right.right = Node(19)
       root.right.right = Node(6)
       root.right.right.left = Node(9)