#delete the prime nodes of a circular llist 
#tc:i/p:8->11->12->13->6
 #   o/p:8->12->6
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def push(head,data):
    n1=node(data)
    temp=head
    n1.data=data
    n1.next=head
    if head!=None:
        while(temp.next!=head):
            temp=temp.next
            temp.next=n1
            
    else:
        n1.next=n1
            
    head=n1
    return head
def d_node(head,delete):
    temp=head
    if (head==delete):
        head=delete.next
        while(temp.next!=delete):
            temp=temp.next
        temp.next=delete.next
        
        return head
def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
 
    if (n % 2 == 0 or n % 3 == 0):
        return False
 
    for i in range(5, n + 1, 6):
        if (i * i < n + 2 and (n % i == 0 or n % (i + 2) == 0)):
            return False
    return True
    
def delpn(head):
    n1=head
    next = n1.next
    n1 = next
    while (n1 != head):
        if (isPrime(n1.data) == True):
            d_node(head, n1)
 
        
        next = n1.next
        n1 = next
 
    return head

def printlist(head):
    temp = head
    if (head != None) :
        print(temp.data, end = " ")
        temp = temp.next
        while (temp != head):
            print(temp.data, end = " ")
            temp = temp.next

            
if __name__=='__main__':
 
    # Initialize lists as empty
    head = None
 
    # Created linked list will be
    # 9.11.32.6.13.20
    head = push(head, 20)
    head = push(head, 13)n
    head = push(head, 6)
    head = push(head, 32)
    head = push(head, 11)
    head = push(head, 9)
    printList(head)
    head = delp(head)
    printList(head)