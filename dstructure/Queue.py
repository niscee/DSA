class Queue:
    def __init__(self) -> None:
        self.queue = []


    def enqueue(self, val):
        self.queue.append(val)



    def printItem(self):
        for item in self.queue:
            print(item)


    def dequeue(self):
        del self.queue[0]       



obj = Queue()
FLAG = True

while FLAG:
    try:
        response = input(" <'E' For Enqueue>  <'D' for Dequeue> <'P' For Print> : ").upper()
        if response == "E":
            getItem = input("Enter Item: ")
            obj.enqueue(getItem)
            print("[Item has been inserted.]")

        if response == "D":
            obj.dequeue()
            print("[Item has been removed.]")

        if response == "P":
            obj.printItem()
    except:
        print("Enter Correct Input!!")





