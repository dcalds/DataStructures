# Linked Lists with Big O

# Create Node object with value(info) and pointer to next
class Node(object):
    def __init__(self,info):
        self.info = info
        self.next = None

# Create a Linked List poiting to None and length zero
class LinkedList(object):
    def __init__(self):
        self.start = None
        self.length = 0

    # Insert pointing to the start node [O(1)]
    def insertStart(self, info):
        newNode = Node(info)

        if not self.start:
            self.start = newNode
        else:
            newNode.next = self.start
            self.start = newNode

        self.length += 1

    # Insert pointing to the None state [O(n)]
    def insertEnd(self, info):
        newNode = Node(info)
        actualNode = self.start

        while actualNode.next is not None:
            actualNode = actualNode.next

        actualNode.next = newNode
        self.length += 1

    # Remove node with same info [O(n)]
    def remove(self, info):

        if self.start is None:
            return

        actualNode = self.start
        previousNode = None

        while actualNode.info != info:
            previousNode = actualNode
            actualNode = actualNode.next

        if previousNode is None:
            self.start = actualNode.next
        else:
            previousNode.next = actualNode.next
        self.length -= 1

    # Returns the length of the list [O(1)]
    def countFast(self):
        return self.length

    # Returns the length of the list by traversing it [O(n)]
    def count(self):
        actualNode = self.start
        length = 0
        
        while actualNode is not None:
          actualNode = actualNode.next
          length += 1
          
        return length

    # Show all the list
    def show(self):
        actualNode = self.start

        while actualNode is not None:
            print('%s' % actualNode.info)
            actualNode = actualNode.next
            
    # Creat a list
    def create(self):
        n = int(input("Enter the number of elements: "))

        if n == 0:
            return
        else:
            for i in range(1, n+1):
                info = int(input("Enter with a new element: "))
                self.insertEnd(info)
