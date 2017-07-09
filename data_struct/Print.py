from myQueue import Queue
import random

class Printer:
    def __init__(self, ppm):
        # ppm: pages/minute
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    def busy(self):
        return self.currentTask != None
    
    def startNext(self, newtask):
        self.currentTask   = newtask
        self.timeRemaining = newtask.getPages()*60.0/self.pagerate

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)
    def getStamp(self):
        return self.timestamp
    def getPages(self):
        return self.pages
    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def newPrintTask():
    return random.randrange(1,181) == 180

def simulation(numSeconds, pagesPerMinute):
    printer      = Printer(pagesPerMinute)
    printQueue   = Queue()
    waitingtimes = []
    for currentSecond in range(numSeconds):
        if newPrintTask():
            new_task = Task(currentSecond)
            printQueue.enqueue(new_task)
        if (not printer.busy()) and (not printQueue.isEmpty()):
            next_task = printQueue.dequeue()
            waitingtimes.append(next_task.waitTime(currentSecond))
            printer.startNext(next_task)
        printer.tick()
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print('Average wait %6.2f secs %3d tasks remaining'%(averageWait, printQueue.size()))

for i in range(30):
    simulation(3600, 10)

