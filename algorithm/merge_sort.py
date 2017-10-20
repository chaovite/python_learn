"""merge sort"""
# This algorithm has O(nlog(n)) complexity

def merge_sort(A):
    """use top down approach to implement merge sort"""
    if len(A) <= 1:
        return A
    # Divide the list into two parts
    n     = len(A)
    left  = merge_sort(A[0:(n//2)])
    right = merge_sort(A[(n//2):])
    return merge(left, right)

def merge(left, right):
    """merge two sorted list in linear space and time"""
    B = []
    while left and right:
        if left[0] < right[0]:
            B.append(left.pop(0))
        else:
            B.append(right.pop(0))
    while left:
        B.append(left.pop(0))
    while right:
        B.append(right.pop(0))
    return B

a = [38, 27, 43, 3, 9, 82, 10]
b = []
c = [2,3,2]
d = [3]
print(merge_sort(a))
print(merge_sort(b))
print(merge_sort(c))
print(merge_sort(d))

    
