"""Find the closest pairs using divide and conquer"""
def closest1d(A):
    """Find the closest pair in 1D"""
    # sort the list once:
    A.sort()
    return find_closest1d(A, 0, len(A) - 1)

def find_closest1d(A, lo, hi):
    """find closest pair of points in a sorted list A"""
    # This subarray is A[lo:hi+1]
    n = hi - lo + 1
    if n == 2:
        return (A[lo], A[hi]), A[hi] - A[lo]
    if n == 1:
        return (None, None), float('inf')
    
    i_l = lo + n//2 - 1
    i_r = lo + n//2

    pair_l, dist_l = find_closest1d(A, lo, i_l)
    pair_r, dist_r = find_closest1d(A, i_r, hi)
    pair_i = (i_l, i_r)
    dist_i = A[i_r] - A[i_l]
    if dist_l < dist_r:
        pair_closest = pair_l
        dist_closest = dist_l
        if dist_i < dist_l:
            pair_closest = pair_i
            dist_closest = dist_i
    else:
        pair_closest = pair_r
        dist_closest = dist_r
        if dist_i < dist_r:
            pair_closest = pair_i
            dist_closest = dist_i
    
    return pair_closest, dist_closest

def closest2d(A):
    """
    find the closest pairs in 2D given a list of points
    A is a list of tuples containing (x , y) coordinates of points
    """
    # To be implemented
    
def find_closest2d(A):
    """
    Points in A are sorted in x already
    """




a = [1, 5, 8, 0, 3, 20]
b = [3, 5, 2]
c = [5, 3]
pair, dist = closest1d(a)
print(a, pair, dist)
pair, dist = closest1d(b)
print(b, pair, dist)
pair, dist = closest1d(c)
print(c, pair, dist)
