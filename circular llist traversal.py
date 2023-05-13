#traversal of a circular llist
class node(object):
    def __init__(self,val):
        self.val=val
        self.next=None
        
class cll:
    def __init__(self):
        self.head=None
    def push(self,val,temp=None):
        if self.head==None:
            nod=node(val)
            self.head=node
            nod.next=self.head
            return
        if temp==None:
            temp=self.head
        if temp.next==self.head:
            
            
            
    def traverse(self,temp=None):
        if temp==None:
            temp=self.head
        if temp.next==self.head:
            print(temp.val,end=)
            