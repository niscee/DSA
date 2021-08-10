class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    # def inserting node.
    def insert_node(self, data):
        if self.value is None:
            self.value = Tree(data)
        else:
            if self.value > data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert_node(data)

            elif self.value < data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert_node(data)



    # printing all node in tree.
    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()

        print(self.value, end=", ")

        if self.right is not None:
            self.right.print_tree()


    # getting minimum value from tree.
    def get_min_value(self):
        if self.left is not None:
            return self.left.get_min_value()
        
        return self.value



    # delete node from tree.
    def delete_node(self, target, parent=None):
        if target > self.value:
            if self.right is not None:
                self.right.delete_node(target, self)
        elif target <  self.value:
            if self.left is not None:
                self.left.delete_node(target, self) 
        else:
            if self.right is not None and self.left is not None:
                self.value = self.right.get_min_value()
                self.right.delete_node(self.value, self)
            elif parent.right == self:
                parent.right = self.right if self.right is not None else self.left
            elif parent.left == self:
                parent.left = self.right if self.right is not None else self.left
                         







obj1 = Tree(10)
obj1.insert_node(5)
obj1.insert_node(15)
obj1.insert_node(2)
obj1.insert_node(1)
obj1.insert_node(22)
obj1.insert_node(13)
obj1.insert_node(14)
obj1.print_tree()
print("\n")


print("\nAfter Deletion.....")
obj1.delete_node(22)
obj1.print_tree()
