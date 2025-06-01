class node:
    def __init__(self, data):
        self.data=data
        self.next=None
        
class linkedlists:
    def __init__(self):
        self.head=None
        self.lenth=0
        
    def isempty(self):
        return self.head==None
        
    def addnode(self, node):
        if self.isempty():
            self.head=node
        elif self.lenth == 1
             self.head.next = node
        else :
            current = self.head
            
        current.next=node
        self.lenth+=1
        
        def search(self, data):
            current= self.head
            while current!=None:
             if current.data == data:
                 break
             current=current.next
            return current
        def printlist(self):
            current=self.head
            while current != None:
                print(current.data)
                current=current.next
                
        def removenode(self, value):
            if self.isempty():
                return None
            current = self.head
            prev = None
            
            if current.data == value:
               self.head = current.next
               current.next=None
               
            self.lenth -=1
            return current
            prev=current
            current=current.next
            

            
            
            
            
            
    
    