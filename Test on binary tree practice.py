class Binary_Tree:
    def __init__ (self, val = None ):
        self.value = val

        if self.value:
            self.left = Binary_Tree()
            self.right = Binary_Tree()
        else:
            self.left = None
            self.right = None

    def isemptyI(self):
        return self.value is None
    
    #if the node is empty, insert the data here
    def insert(self, data):
        if self.isempty():
            self.value = data

     #create left and right children
            self.left  = Binary_Tree()
            self.right = Binary_Tree()

            print("{} is inserted".format(self.value))

    #if data is less than current node value,
    #insert into left subtree
        elif data < self.value:
            self.left.insert(data)
            return
        
    #if data is greater than current node value,
    #insert into left subtree

        elif data > self.value:
            self.right.insert(data)
            
    
    #if data is equal to the current node value,
    #do nothing
        
        elif data == self.value:
    