#program of single llist
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class llist:
    def __init__(self):
        self.head=None
    def oplist(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
            
#if __name__=='__main__':
    ll=llist()
    ll.head=node(1)
    sec=node(2)
    thi=node(3)
    ll.head.next=sec
    sec.next=thi
    ll.oplist()
            