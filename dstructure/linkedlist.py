class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head  


    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next          


    def add(self, value, index):
        current = self.head
        counter = 1
        while current:
            if counter == index-1:
                newobj = Node("tue")
                tempnext = current.next
                current.next = newobj
                newobj.next = tempnext

            current = current.next
            counter += 1


# creating class.
obj1 = Node("sun")
obj2 = Node("mon")
obj3 = Node("wed")

# assigning next location of each class object.
obj1.next = obj2
obj2.next = obj3

# assigning head node.
mainobj = LinkedList(obj1)
mainobj.print()
mainobj.add("tue", 3)
print("-------------After adding new value-------------------")
mainobj.print()