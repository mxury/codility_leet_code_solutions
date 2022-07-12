"""
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers,
specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].
We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point
(assuming that the discs contain their borders).
The figure below shows discs drawn for N = 6 and A as follows:
  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0
There are eleven (unordered) pairs of discs that intersect, namely:
        discs 1 and 4 intersect, and both intersect with all the other discs;
        disc 2 also intersects with discs 0 and 3.
Write a function:

    def solution(A)

that, given an array A describing N discs as explained above, returns the number of
(unordered) pairs of intersecting discs. The function should return −1 if the number
of intersecting pairs exceeds 10,000,000.
Given array A shown above, the function should return 11, as explained above.
Write an efficient algorithm for the following assumptions:
    N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [0..2,147,483,647].
"""
from time_dec import timer_func

@timer_func
def solution(A):
    n = len(A)
    pairs = 0
    for i in range(n):
        current = i + A[i]
        for j in range(i+1,n):
            if current > j - A[j]:
                if pairs > 1e7:
                    return -1
                pairs += 1

    return pairs

# @timer_func
def solution_2(A):
    n = len(A)
    points = [[centre - radius, centre + radius] for radius, centre in enumerate(A)]
    points.sort()
    pairs = 0
    print(points)
    for i, ends in enumerate(points):
        for j in range(i+1, n):
            if ends[1] >= points[j][0]:
                if pairs <= 1e7:
                    print(f'ends[{i}][1]: {ends[1]}')
                    print(f'points[{j}][0]: {points[j][0]}')
                    pairs += 1
                else:
                    return -1
            else:
                break
    return pairs

A = [1,5,2,1,4,0]

print(solution_2(A))
print(solution(A))

