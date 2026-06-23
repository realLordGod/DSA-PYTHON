class Node:
    def __init__(self,value=None,next=None,prev=None):
        self.value = value
        self.next = next
        self.prev=prev

    
class DoublyLL:
    def __init__(self):
        self.head = None

    
    def InsertAtEnd(self,value):
        temp=Node(value)
        if self.head == None:
            self.head = temp
            return
        
        t=self.head
        while(t.next !=None):
            t=t.next

        t.next=temp
        temp.prev = t


    def insertAtBeg(self,val):

        temp = Node(val)

        if self.head ==None:
            self.head = temp
            return
        

        temp.next=self.head
        self.head.prev=temp
        self.head = temp


    
    def inserAtMid(self,val,x):
        temp=Node(val)

        t =  self.head

        while t:


            if t.value==x:
                break

            else:
                t=t.next

        
        temp.next=t.next
        if t.next:
            t.next.prev=temp
        t.next = temp
        temp.prev=t


    
    def deletionDLL(self,val):
        if self.head==None:
            print("Nothing to Delete Empty Linked List")
            return







    def printLL(self):
        t=self.head

        while t:
            print(t.value)
            t=t.next
        


        
