
from collections import deque

class Queue:

    def __init__(self):
        self.items=deque()

    def isEmpty(self):
        if len(self.items)==0:
            return True
        
        else:
            return False
        
    def insertion(self,val):
        self.items.append(val)


    def delete(self):
        if self.isEmpty():
            raise Exception("queue is empty")
        
        else:
            return self.items.popleft()
        

    


#Deque--->


class Deque:

    def __init__(self):
        self.items=deque()

    def isEmpty(self):
        if len(self.items)==0:
            return True
        
        else:
            return False
        
    def insertionInfront(self,val):
        self.items.insert(0,val) # self.items.appendleft(val)

    def deleteFromFront(self):
        if self.isEmpty():
            raise Exception("empty")
        else:

            self.items.popleft()

    def insertionAtEnd(self,val):
        self.items.append(val)

    def deleteatlast(self):
        if  self.isEmpty():
            raise Exception("empty")
            
        else:    
            self.items.pop()

        
    


