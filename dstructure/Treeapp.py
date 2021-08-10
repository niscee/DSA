class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



    # inserting new node in the tree.
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

    
    
    #searching for the specific node.
    def find_node(self, data):
        if self.data == data:
            return True

        if self.data > data:
            if self.left is None:
                return False

            return self.left.find_node(data)

        if self.data < data:
            if self.right is None:
                return False

            return self.right.find_node(data)



    #get the nearest node of target value.
    def closest_node(self, target):
        current_node = self
        closeval = current_node.data

        while current_node:
            if abs(target - closeval) > abs(target - current_node.data):
                closeval = current_node.data

            if target > current_node.data:
                current_node = current_node.right

            elif target < current_node.data:
                current_node = current_node.left

            else:
                break

        return closeval


    # printing each node in the tree.
    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()

        print(self.data, end=" ")

        if self.right is not None:
            self.right.print_tree()


            
    # finding min value from the tree.
    def min_node(self):
        if self.left is None:
            return self.data

        return self.left.min_node()
        




# initializing node.
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

print("--------------------------------------------------")


#finding value.
result1 = obj1.find_node(14)
print("Given value is Found.") if result1 else print(
    "Given value is not in the Tree.")


print("--------------------------------------------------------------------")

#finding closest value.
result2 = obj1.closest_node(3)
print("closest value: ", result2)


print("--------------------------------------------------------------------")

#finding min value in the tree.
result3 = obj1.min_node()
print("Minimum value: ", result3)





