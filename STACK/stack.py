class Stack:

    def __init__(self):
        self.s=[]

    def Length(self):
        return len(self.s)
    
    def push(self,val):
        self.s.insert(0,val)

    def isEmpty(self):
        if len(self.s)==0:
            return True
        
        else:
            return False

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        
        else:
            return self.s[0]


    def pop(self):
        if self.isEmpty():
            raise Exception("stack is empty")
        
        else:
            return self.s.pop(0)
        



# another method 


class StackNew:

    def __init__(self):
        self.s=[]

    def length(self):
        return len(self.s)
    

    def isEmpty(self):
        if len(self.s)==0:
            return True
        else:
            return False
        

    def push(self,x):
        self.s.append(x)

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        
        else:
            print(self.s[-1])


    def pop(self):
        if self.isEmpty():
            raise Exception("stack is empty")
        
        else:
            return self.s.pop(-1)



