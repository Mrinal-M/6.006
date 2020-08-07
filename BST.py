class AVL_Tree:
    def __init__(self,node):
        self.root=node
    
    def check(self,node):
        while node != None:
            if node.left_height-node.right_height>1:
                if node.left.left_height>node.left.right_height:
                    self.right_rotate(node)
                elif node.left.left_height<node.left.right_height:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            if node.right_height-node.left_height>1:
                if node.right.right_height>node.right.left_height:
                    self.left_rotate(node)
                elif node.right.right_height<node.right.left_height:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node=node.parent

    def insert(self,key):
        new = Node(key)
        node=self.root
        while(True):
            if new.val>=node.val:
                if node.right is None:
                    node.right=new
                    new.parent=node
                    new.depth=new.parent.depth+1
                    self.update_height(new.parent)
                    self.check(new)
                    break
                else:
                    node=node.right
            else:
                if node.left is None:
                    node.left=new
                    new.parent=node
                    new.depth=new.parent.depth+1
                    self.update_height(new.parent)
                    self.check(new)
                    break
                else:
                    node=node.left

    def update_depth(self,root):
        root.depth-=1
        if root.left != None:
            self.update_depth(root.left)
        if root.right != None:
            self.update_depth(root.right)

    def height(self,node):
        if node==None:
            return -1
        else:
            return(max(self.height(node.left),self.height(node.right))+1)

    def update_height(self,root):
        while root != None:
            root.height=self.height(root)
            root.left_height=self.height(root.left)
            root.right_height=self.height(root.right)
            root=root.parent
    

    def left_rotate(self,node):
        if node.parent == None:
            node.right.parent= None
            self.root=node.right
        else:
            node.right.parent=node.parent
            if node.parent.right==node:
                node.parent.right=node.right
            else:
                node.parent.left=node.right
        node.parent=node.right
        if node.parent.left !=None:
            node.right=node.parent.left
            node.right.parent=node
        else:
            node.right=None
        node.parent.left=node
        self.update_height(node)


    def right_rotate(self,node):
        if node.parent == None:
            node.left.parent = None
            self.root=node.left
        else:
            node.left.parent=node.parent
            if node.parent.right==node:
                node.parent.right=node.left
            else:
                node.parent.left=node.left
        node.parent=node.left
        if node.parent.right != None:
            node.left=node.parent.right
            node.left.parent=node
        else:
            node.left=None
        node.parent.right=node
        self.update_height(node)
    
    def delete_min(self):
        if self.root != None:
            node=self.root
            while(node.left!=None):
                node=node.left
            if node==self.root:
                self.root=node.right
                node.right.parent=None
                self.update_depth(node.right)
            else:
                if node.right is None:
                    node.parent.left=None
                    node.disconnect()
                else:
                    node.parent.left=node.right
                    self.update_depth(node.right)
                    node.disconnect()
    def delete_max(self):
        if self.root!=None:
            node=self.root
            while(node.right!=None):
                node=node.right
            if node==self.root:
                self.root=node.left
                node.left.parent=None
                self.update_depth(node.left)
            else:
                if node.left is None:
                    node.parent.right=None
                    node.disconnect()
                else:
                    node.parent.right=node.left
                    self.update_depth(node.left)
                    node.disconnect()
        
    def isthere(self,k):
        if self.root!=None:
            node=self.root
            while(node != None):
                if node.val==k:
                    return (True,node)
                elif node.val<k:
                    node=node.right
                else:
                    node=node.left
            return (False,None)
        else:
            return (False,None)

    def search(self,k):
        (a,b)=self.isthere(k)
        if a==True:
            return b
        else:
            return None

    def inorder(self,root):
        if root !=None:
            self.inorder(root.left)
            print((root.val,root.height)),
            self.inorder(root.right) 
    
    def preorder(self,root):
        if root != None:
            print(root.val),
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val),


class Node:
    def __init__(self,key):
        self.disconnect()
        self.val=key
        
    def disconnect(self):
        self.parent=None
        self.left=None
        self.right=None
        self.depth=0
        self.height=0
        self.left_height=-1
        self.right_height=-1


    
tree=AVL_Tree(Node(10))

import random
array=[]
while len(array)<100:
    temp=random.randint(1,1000)
    if temp not in array:
        array.append(temp)
# tree.insert(5)
# tree.insert(15)
# tree.insert(46)
# tree.insert(47)
# tree.insert(3)
# tree.insert(4)
# tree.insert(8)
# tree.insert(7)
# tree.insert(44)
# tree.insert(48)
# tree.insert(1)
#tree.inorder(tree.root)
# tree.insert(2)
for i in array:
    tree.insert(i)
array.sort()
print(array)
# ar=[48, 27, 19, 49, 50, 7, 12, 6, 29, 15, 46, 28, 47, 14, 25, 3, 23, 21, 36, 34, 38, 30, 33, 9, 35, 24, 2, 26, 22, 16]
# for i in ar:
#     tree.insert(i)
# n=tree.search(30)
# print(n.parent.val)
# tree.insert(8)
# tree.insert(15)
# tree.insert(20)
# tree.insert(18)
# n=tree.search(30)
# print(n.parent.val)
tree.inorder(tree.root)
# tree.delete_min() 
# tree.delete_max()
# tree.delete_max()#
# tree.delete_max()
# tree.inorder(tree.root)
#print(tree.search(10).left.left.val)


