from myDeque import Deque
def palchecker(aString):
    cdeque = Deque()
    for ch in aString:
        cdeque.addRear(ch)
    eq = True
    while cdeque.size()>1 and eq:
        first = cdeque.removeFront()
        last  = cdeque.removeRear()
        if first!=last:
            eq = False
    return eq

print(palchecker('lsdkjfskf'))
print(palchecker('radar'))
