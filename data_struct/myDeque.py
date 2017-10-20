# Implement a deque using python list
class Deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items)==0
    def addFront(self,item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0,item)
    def removeFront(self):
        self.items.pop()
    def removeRear(self):
        self.items.pop(0)
    def size(self):
        return len(self.items)
