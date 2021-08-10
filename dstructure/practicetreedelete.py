class Tree:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


    # insert new node in Tree.
    def insert_node(self, data):
        if self.data is None:
            self.data = Tree(data)
        else:
            if self.data > data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert_node(data)
            else:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert_node(data)        



    # print every node in the Tree.
    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()

        print(self.data, end=" ")

        if self.right is not None:
            self.right.print_tree() 

    

    # returns the minimum value in the Tree.
    def get_min_val(self):
        if self.left is None:
            return self.data

        return self.left.get_min_val()       



    # delete the specified node from the Tree.
    def delete_node(self, target, parent=None):
        if target < self.data:
            if self.left is not None:
                self.left.delete_node(target, self)
        elif target > self.data:
            if self.right is not None:
                self.right.delete_node(target, self)
        else:
            if self.left is not None and self.right is not None:
                self.data = self.right.get_min_val()
                self.right.delete_node(self.data, self)

                
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right









obj1 = Tree(10)
obj1.insert_node(5)
obj1.insert_node(15)
obj1.insert_node(2)
obj1.insert_node(5)
obj1.insert_node(1)
obj1.insert_node(22)
obj1.insert_node(13)
obj1.insert_node(14)
obj1.print_tree()       


print("\nAfter Deletion.....")
obj1.delete_node(10)
obj1.print_tree()