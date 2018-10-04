class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SList:
    def __init__(self,value):
        node = Node(value)
        self.head = node
    def addNode(self,value):
        node = Node(value)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = node
        return self
    def printAllValues(self,msg=""):
        runner = self.head
        print(msg)
        print(f"head points to {id(self.head)}")
        while runner.next != None:
            print(f"{id(runner)}, {runner.value}, {(id(runner.next))}")
            runner = runner.next
        print(f"{id(runner)}, {runner.value}, {(id(runner.next))}")
        return self
    def removeNode(self,value):
        runner = self.head
        if runner.value == value:
            self.head = runner.next
            return self
        while runner.next.value != value:
            runner = runner.next
        if runner.next.next == None:
            runner.next = None
            return self
        else:
            runner.next = runner.next.next
        return self
    def insertNode(self,value,index):
        runner = self.head
        node = Node(value)
        if index == 0:
            node.next = self.head
            self.head = node
            return self
        count = 0
        while count + 1 != index:
            runner = runner.next
            count += 1
        node.next = runner.next
        runner.next = node
        return self

list = SList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.addNode(22)
list.removeNode(1)
list.removeNode(9)
list.insertNode(3,0)

list.printAllValues("Attempt 1")
