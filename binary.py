class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def PrintTree(self):
      print(self.data)

def ifNodeExists(node, key):
 
    if (node == None): 
        return False
 
    if (node.data == key): 
        return True
 
    res1 = ifNodeExists(node.left, key) 
    if res1:
        return True

    res2 = ifNodeExists(node.right, key) 
 
    return res2
root=Node(7)
root.left=Node(3)
root.right=Node(9)

key=1

if(ifNodeExists(root,key)):
    print("Key found")
else:
    print("Key not found")



    
    