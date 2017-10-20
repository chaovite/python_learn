"""
Count the number of inversion in a list of integers
"""
# This function can be optimized by passing indeces in the recursion 
# rather than creating intermediate lists.

def merge(left, right):
    """merge two sorted list in linear space and time"""
    B = []
    cnt = 0
    while left and right:
        if left[0] < right[0]:
            B.append(left.pop(0))
        else:
            #inversion
            cnt += len(left)
            B.append(right.pop(0))
    while left:
        B.append(left.pop(0))
    while right:
        B.append(right.pop(0))
    return B, cnt

def count_inversion(A):
    """count # of inversions in A"""
    # handle basecases:
    n = len(A)
    if n < 2:
        return 0, A
    if n == 2:
        if A[0] > A[1]:
            # swap lo and hi
            B = A[::-1]
            return 1, B
        else:
            return 0, A
    # n > 2, divid and conquer
    cnt_l, l = count_inversion(A[: n//2])
    cnt_r, r = count_inversion(A[n//2 :])
    m, cnt_m = merge(l, r)
    return cnt_l + cnt_r + cnt_m, m
    
A = [2, 4, 1, 3, 5]
B = [1, 20, 6, 4, 5]
print(count_inversion(A))
print(count_inversion(B))
