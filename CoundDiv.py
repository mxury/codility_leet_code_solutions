"""
Write a function:

    def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K,
 i.e.:
    { i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by
2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A ≤ B.
"""


def solution(A, B, K):
    if not (A - B):
        if not A % K:
            return 1
        else:
            return 0
    return (B - A ) // K + 1


def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

A, B, K = [10, 14, 2]


print(solution(A, B, K))
