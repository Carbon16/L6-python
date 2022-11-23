#linear queue class
class LinearQueue:
    def __init__(self):
        self.queue=[]
    def isEmpty(self):
        return self.queue==[]
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        data=self.queue[0]
        del self.queue[0]
        return data
    def size(self):
        return len(self.queue)
    def peek(self):
        return self.queue[0]
    def display(self):
        print(self.queue)


print(" killlllllllllllllllllll mmmmmmmmmmmmme ") 