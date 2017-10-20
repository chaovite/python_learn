"""compute the median of two sorted list of the same size"""
# This an implementation using principals of divide and conquer
def median_merge(A, B):
    """A, B are sorted"""
    n   = len(A)
    if n == 1:
        return (A[0] + B[0])//2
    m_a = median_s(A)
    m_b = median_s(B)
    if n%2==0:
        n_left  = int(n//2)
        n_right = int(n//2)
    else:
        n_left  = int(n//2) 
        n_right = int(n//2 + 1)
    if m_a == m_b:
        return m_a
    elif m_a > m_b:
        left  = B[n_left:]
        right = A[0:n_right]
    else:
        left  = A[n_left:]
        right = B[0: n_right]
    return median_merge(left, right)

def median_s(A):
    """get the median of a sorted list"""
    n = int(len(A))
    if n == 0:
        return None
    if n%2 == 0:
        return (A[n//2-1] + A[n//2])//2
    else:
        return A[n//2]

A = [1, 2, 3, 5, 6, 9, 10]
B = [5, 9, 10, 11, 16, 20, 24]
print(sorted(A+B))
print(median_merge(A, B))
