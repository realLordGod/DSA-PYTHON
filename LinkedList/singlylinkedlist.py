class Node:

    def __init__(self,val,next=None):
        self.val=val
        self.next=next


    
class SinglyLinkedList:

    def __init__(self,head=None):
        self.head = head


    def insertAtBeg(self,val):
        self.head = Node(val,self.head)

    def insertInMid(self,val,x):
        temp = Node(val)
        t1 = self.head
        while t1:
            if t1.val == x:
                temp.next=t1.next
                t1.next=temp
                break

            t1 = t1.next


    def inserAtEnd(self,val):
        temp=Node(val)

        t1=self.head

        if self.head!=None:
            while t1:
                if t1.next==None:
                    t1.next=temp
                    return
                t1=t1.next

        else:
            self.head=temp

    def deleteLL(self,val):

        if self.head ==None:
            return
        
        if self.head.val == val:
            self.head = self.head.next
            return





        t1=self.head
        prev=t1

        while t1:
            if t1.val == val:
                prev.next = t1.next
                return
                
            else:
                prev=t1
                t1=t1.next


    def Printall(self):

        t1=self.head

        while t1:
            print(t1.val)
            t1=t1.next
            



    
    

            
        

        