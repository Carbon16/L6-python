#circular queue class

class CircularQueue:
    def __init__(self):
        self.queue=[]
        self.head=0
        self.tail=0
    def isEmpty(self):
        return self.queue==[]
    def enqueue(self,data):
        self.queue.append(data)
        self.tail+=1
    def dequeue(self):
        data=self.queue[self.head]
        self.head+=1
        return data
    def size(self):
        return len(self.queue)
    def peek(self):
        return self.queue[self.head]
    def display(self):
        print(self.queue)
        
#main program
queue=CircularQueue()
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Size")
    print("4. Display")
    print("5. Quit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        data=input("Enter data: ")
        queue.enqueue(data)
    elif choice==2:
        data=queue.dequeue()
        print("Popped data is: ",data)
    elif choice==3:
        print("Size of queue is: ",queue.size())
    elif choice==4:
        queue.display()
    elif choice==5:
        break
    else:
        print("Invalid!")