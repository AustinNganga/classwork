class Singlylinkedlist:
    def __init__(self,value,nextnode=None):
        self.value=value
        self.nextnode=nextnode


snode1=Singlylinkedlist(1)
snode2=Singlylinkedlist(2)
snode3=Singlylinkedlist(3)
snode4=Singlylinkedlist(4)


snode1.nextnode=snode2
snode2.nextnode=snode3
snode3.nextnode=snode4

currentnode=snode1

while True:
    print(currentnode.value,">>>", end=' ')
    if currentnode.nextnode is None:
        print("None")
        break

    currentnode=currentnode.nextnode

