"""
2588번 곱셈
"""

A = int(input())
B = int(input())

digit = list(map(int, list(str(B))))

for i in range(3):
    print(A * digit[2 - i])

print(A * B)
