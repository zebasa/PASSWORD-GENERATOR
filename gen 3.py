import random
upper_case_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case_letters=upper_case_letters.lower()
symbols="!£$%^&*()@':;#~///><"
numbers="123456789"
upper,lower,sims,numero=True,True,True,True
gen=""
if upper:
    gen+=upper_case_letters
if lower:
    gen+=lower_case_letters
if sims:
    gen+=symbols
if numero:
    gen+=numbers
length=20
amount=40
for x in range(amount):
    x="".join(random.sample(gen,length))
    print(f"passsword:{x}")


class Node:
    def __init__(self,head):
        self.head=head
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
def insertbeginning(self,new_data):
    new_node=Node(new_data)
    new_node.Next=self.head
    self.head=new_node
def print(self):
    temp=self.head
    whiile temp:
        print(temp.data, end="")
        temp=temp.Next
    print()
if __name__="__main__":
    llist=linkedlist()
     llist.insertAtBeginning('fox') 
    llist.insertAtBeginning('brown')
    llist.insertAtBeginning('quick')  
    llist.insertAtBeginning('the')  
