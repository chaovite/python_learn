# hot Potato problem
from myQueue import Queue
def hotPotato(namelist, num):
    queue = Queue()
    for name in namelist:
        queue.enqueue(name)
    while queue.size()>1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        out=queue.dequeue()
    return queue.dequeue()

namelist = ['Bill','David','Susan','Jane','Kent', 'Brad']
print(hotPotato(namelist, 7))
