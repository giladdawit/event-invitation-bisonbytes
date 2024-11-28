#1
class Binary_Tree:
    def __init__(self,val=None):

        self.value = val

        if self.value:
            self.left = Binary_Tree()
            self.right = Binary_Tree()
        else:
            # If the node has no value, the left and right = Null

            self.left = None
            self.right = None

    #check if node is empty
    def isempty(self):
        return self.value is None
    
    #insert a new value into the tree
    def insert(self, data):

        #if the node is empty, insert the data here
        if self.isempty():
            self.value = data

            #create left and right children

            self.left = Binary_Tree()
            self.right = Binary_Tree()
            print("{} is inserted".format(self.value))
        
        #if data is less than current node value,
        #insert into left subtree
        elif data < self.value:
            self.left.insert(data)
            return 
        # if data is greater than current node value,
        # insert into right subtree
        elif data > self.value:
            self.right.insert(data)

        #if data is equal to current node value, do nothing
        elif data == self.value:
            return
#2     
    #In-order traversal: left - root - right
    def inorder(self):
        if not self.isempty():
            result = []
            if self.left:
                result.extend(self.left.inorder())
            result.append(self.value)
            if self.right:
                result.extend(self.right.inorder())
            return result
        return []   
       
    #Preorder traversal: root - left - right
    def preorder(self):
        if not self.isempty():
            result = [self.value]
            if self.left:
                result.extend(self.left.preorder())
            if self.right:
                result.extend(self.right.preorder())
            return result
        return []
    
    #Postorder Traversal: left - right - root 
    def postorder(self):
        if not self.isempty():
            result = []
            if self.left:
                result.extend(self.left.postorder())
            if self.right:
                result.extend(self.right.postorder())
            result.append(self.value)
            return result
        return[]
#3
    def find_path(self, target):
        if self.isempty():
            return None
        if self.value == target:
            return [self.value]
           
        if self.left:
            left_path = self.left.find_path(target)
            if left_path:
                return [self.value] + left_path
        if self.right:
            right_path = self.right.find_path(target)
            if right_path:
                return [self.value] + right_path
        return None

tree = Binary_Tree()
data = [15, 10, 20, 8, 12, 17, 25, 6, 9]
for value in data:
    tree.insert(value)

print("In-order Traversal:", tree.inorder())
print("Pre-order Traversal:", tree.preorder())
print("Post-order Traversal:", tree.postorder())

path_12 = tree.find_path(12)  
path_25 = tree.find_path(25)  
path_6 = tree.find_path(6)

print("Path to 12:", path_12)
print("Path to 25:", path_25)
print("Path to 6:", path_6)


            
           