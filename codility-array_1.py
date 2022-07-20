test = [9,3,9,3,9,7,9]

def solution(A):
    xor = 0

    for num in A:
        xor ^= num

    return xor

