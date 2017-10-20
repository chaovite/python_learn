"""
Implement quick sort
"""
def quick_sort1(l):
    # pick the first element to be the pivot
    # this is not efficient because of constantly creating new lists.
    # we should swap elements instead of creating new lists
    if len(l) <= 1:
        return l
    p   = l[0] 
    l_l = [] # list left
    l_r = [] # list right
    i   = 1
    while i<len(l):
        e = l[i]
        if e > p:
            l_r.append(e)
        else:
            l_l.append(e)
        i += 1
    return quick_sort1(l_l) + [p] + quick_sort1(l_r)

def quick_sort2(A, lo, hi):
    # implement quick sort by swapping elements
    # keep the low and high index (inclusively)
    if lo < hi:
        # first partition into two sections.
        p = partition(A, lo, hi)
        quick_sort2(A, lo, p - 1)
        quick_sort2(A, p + 1, hi)

def partition(A, lo, hi):
    # partition A[lo] to A[hi] such that
    # left part from lo to p is smaller than p + 1 to h
    # start pivot as the highest
    pivot = A[hi]
    i = lo - 1
    j = hi + 1
    while j - i > 1:
        if A[j-1] > pivot:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
        elif A[j-1] < pivot:
            A[i+1], A[j-1] = A[j-1], A[i+1]
            i += 1
        else: # A[j-1] =pivot
            j -= 1
    return j
a = [5, 4, 6, 10, 3]
#print(quick_sort1(a))
#print(quick_sort1([1]))
#print(quick_sort1([]))
#print(quick_sort1([3, 1, 2]))

quick_sort2(a, 0, len(a) - 1)
print(a)
a = [1,4,4,3]
quick_sort2(a, 0, 3)
print(a)
