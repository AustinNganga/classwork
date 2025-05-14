class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next


class linkedlist:
    def __init__(self):
        self.head=None

    def insertatthebeginning(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head

        self.head=new_node
    def insertattheend(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            new_node=self.head
            return
        last=self.head
        while last.next:
            last=last.next

        last.next=new_node

    def deletefromthebeginning(self):
        if self.head is None:
            return "linked list is empty"
        self.head=self.head.next


    def deletefromtheend(self):
        if self.head is None:
            return "linked list is empty"
        if self.head.next is None:
            self.head=None
            return
        temp=self.head
        while temp.next.next:
            temp=temp.next

        temp.next=None




    def printlinkedlist(self):
        temp=self.head
        while temp:
            print(temp.data, end=' ')
            temp=temp.next

        print()

if __name__=='__main__':
    llist=linkedlist()
    llist.insertatthebeginning("fox")
    llist.insertatthebeginning("brown")
    llist.insertatthebeginning("quick")
    llist.insertatthebeginning("the")
    llist.printlinkedlist()

    llist.insertattheend("jumps")
    llist.printlinkedlist()
    llist.deletefromtheend()
    llist.printlinkedlist()
    llist.deletefromthebeginning()
    llist.printlinkedlist()



