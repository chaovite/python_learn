"""
Find the median of the merge of two lists of integers with different length
The two lists A, B, are sorted. len(A) <= len(B)
"""
def median_merge_neq(A, B):
    """ N <= M """
    N = int(len(A))
    M = int(len(B))
    # handle base cases
    # A or B are empty
    if N == 0:
        return median_s(B)
    if N == 1:
        a = A[0]
        if M == 1:
            return (a + B[0])//2
        else:
            if M%2 == 0:
                # M is even
                left  = B[M//2 - 1]
                right = B[M//2]
                if a < left:
                    return left
                elif a > right:
                    return right
                else:
                    return a
            else:
                # M is odd
                left  = B[M//2 - 1]
                right = B[M//2 + 1]
                mid   = B[M//2]
                if a < left:
                    return (left + mid)//2
                elif a > right:
                    return (right + mid)//2
                else:
                    return (mid + a)//2
    
    # N >= 2, M >= 2 General cases
    median_a = median_s(A)
    median_b = median_s(B)
    if median_a == median_b:
        return median_a
    elif median_a > median_b:
        return median_merge_neq(A[:-N//2], B[N//2:])
    else:
        return median_merge_neq(A[N//2:], B[:-N//2])
    
def median_s(A):
    """helper function to return the median of a sorted list"""
    n = int(len(A))
    if n == 0:
        # empty list
        return None
    if n%2 == 0:
        return (A[n//2 - 1] + A[n//2])//2
    else:
        return A[n//2]


A = [6, 8, 10, 50, 60, 70]
B = [1, 5,7, 7, 15, 10, 20, 60]
print(A, B)
print(sorted(A+B))
print(median_merge_neq(A, B))
