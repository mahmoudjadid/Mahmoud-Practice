#Q4
class node:
    def __init__(self, data):
        self.data=data
        self.next=None
class linkdedlist:
    def __init__(self):
        self.head=None
        self.lenth=0
    
    def isempty(self):
        return self.head==None
    
    def append(self):
        if self.isempty :
            self.head=node
            self.lenth+=1
        elif self.lenth==1:
            self.head.next=node
            self.lenth+=1
        else :
            current=self.head
            while current.next!=None:
                current=current.next
                current.next=node
                self.lenth+=1
                
 # to reverse the add we need to remove a node

class node:
    def __init__(self, data):
        self.data=data
        self.next=None
class linkdedlist:
    def __init__(self):
        self.head=None
        self.lenth=0
    
    def isempty(self):
        return self.head==None
    
    def removenode(self, value):
        if self.isempty :
            return None
        else :
            current=self.head
            prev=None
            
            if current.data==value:
                self.head=current.next
                current.next=None
                self.lenth-=1
                return current
            
            while current!=None:
                if current==value:
                    prev.next=current.next
                    self.lenth-=1
                    current.next=None
                    return current
                prev=current
                current=current.next
                    
#Question 5 :
# stack :work in order first in last out                 
#        if you want to reach the last node you have to pop the previous nodes all
#        for example its like stacking dishes above each other , if we want to reach the dish at the 
#        so we add nodes to head and pop nodes from head
#         bottom we have to remove all dishes above
#         no tail is deffined
#Queue  :Apply the order of first in first out
#       :if we want to remove a node we must push nodes untill we reach the wanted node
#       :we add nodes for the tail and we remove noddes from the head
#       :it has a head and a tail deffined by zero in the deffinition of code
 


# Q6

class queue:
    def __init__(self):
        self.head=None
        self.tail=None
        
        # the logical eror is we have to define head and tail , not to open a list in items
        
    def enqueue(self):
        if self.head==None and self.tail==None
        self.head=node
        self.tail=node
        
    # the logic if enqueue is to add node , its not a list to append it , 
    
    # the third logical eror is if its empty return none , or remove the head node, and return 
    # the removed node to save it and later use (if needed)
    
            
            
        
            
        