"""
Write a function solution that, given two integers A and B, returns a string containing exactly A letters 'a' and
exactly B letters 'b' with no three consecutive letters being the same (in other words, neither "aaa" nor "bbb"
may occur in the returned string).
Examples:
1. Given A = 5 and B = 3, your function may return "aabaabab". Note that "abaabbaa" would also be a correct answer.
Your function may return any correct answer.
2. Given A = 3 and B = 3, your function should return "ababab", "aababb", "abaabb" or any of several other strings.
3. Given A = 1 and B = 4, your function should return "bbabb", which is the only correct answer in this case.
Assume that:

        A and B are integers within the range [0..100];
        at least one solution exists for the given A and B.
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""

def solution(A,B):
    diff = A - B
    if diff < 0:
        A, B = B, A
        a = 'b'
        b = 'a'
    else:
        a = 'a'
        b = 'b'
    string = str()
    for i in range(1, A - B):
        string += 2 * a + b
        A -= 2
        B -= 1

    while A & B:
        print(A)
        print(B)
        print(string)
        if A != B:
            string += a
            A -= 1
        else:
            if (A==1) & (B==1):
                string += a + b
            else:
                string += 2 * a
    return string

A, B = 7,5

print(solution(A,B))
