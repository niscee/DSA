class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # print tree (inorder travesal).
    def printTree(self):
        if self.left:
            self.left.printTree()

        print(self.data, end=" ")

        if self.right:
            self.right.printTree()



    # print tree (preorder travesal).
    # def printTree(self):
    #     if self.left:
    #         self.left.printTree()

    #     print(self.data, end=" ")

    #     if self.right:
    #         self.right.printTree()



    # print tree (postorder travesal).
    # def printTree(self):
    #     if self.left:
    #         self.left.printTree()

    #     if self.right:
    #         self.right.printTree()

    #     print(self.data, end=" ")

    
    
    # finding item in the tree.
    def findVal(self, data):
        if self.data == data:
            return True

        if self.data < data:
            if self.right is None:
                return False

            return self.right.findVal(data)

        if self.data > data:
            if self.left is None:
                return False

            return self.left.findVal(data)

    
    
    # insert new node in the tree.
    def insertNode(self, data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insertNode(data)

            if self.data < data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insertNode(data)

    
    
    # finding closest value in the tree.
    def findClosest(self, target):
        currentNode = self
        closest = currentNode.data
        while currentNode:
            if abs(target - closest) > abs(target - currentNode.data):
                closest = currentNode.data

            if target < currentNode.data:
                currentNode = currentNode.left

            elif target > currentNode.data:
                currentNode = currentNode.right

            else:
                break

        return closest


# creating object.
obj1 = Tree(10)
obj1.insertNode(5)
obj1.insertNode(15)
obj1.insertNode(2)
obj1.insertNode(5)
obj1.insertNode(1)
obj1.insertNode(22)
obj1.insertNode(13)
obj1.insertNode(14)
obj1.printTree()

print("--------------------------------------------------")


# finding value.
result = obj1.findVal(9)
print("Given value is Found.") if result else print(
    "Given value is not in the Tree.")


print("--------------------------------------------------------------------")

# finding closest value.
result = obj1.findClosest(16)
print(result)
