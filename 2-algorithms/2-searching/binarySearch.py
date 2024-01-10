class Person:
    def __init__(self, weight,name, hairColor, skinColor,):
          self.name = name
          self.weight = weight
          self.hairColor = hairColor
          self.skinColor = skinColor
 
         


ali =  Person(weight=100,skinColor="brown",hairColor="orange",name="Ali")
print(ali.name)

# ali.hairColor = ""
# ali.height = ""
# ali.name = ""
# ali. = ""






# # value, left and right
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# # Create the binary tree
# class BinerySearchTree:
#     def __init__(self):
#         self.root  = None
#     def insert(self,value):
#         new_node = Node(value)
#         if self.root == None:
#             self.root = new_node
#             return True
#         temp = self.root
#         while True:
#             if new_node.value ==temp.value:
#                 return False
#             if new_node.value<temp.value:
#                 if temp.left ==None:
#                     temp.left = new_node
#                     return True
#                 temp = new_node
#             else:
#                 if temp.right ==None:
#                         temp.right = new_node
#                         return True
#                 temp = new_node

# my_Tree =  BinerySearchTree()
# print(my_Tree.insert(5))
# print(my_Tree.insert(2))
# print(my_Tree.insert(6))
# print(my_Tree.insert(9))
# print(my_Tree.root.value)        
# print(my_Tree.root.left.value)        
# print(my_Tree.root.right.value)        
         