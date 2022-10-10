"""
25304번 영수증
"""

X = int(input())
N = int(input())

total = 0

for _ in range(N):
    A, B = map(int, input().split())

    total += A * B

if X == total:
    print("Yes")
else:
    print("No")
