"""
2525번 오븐 시계
"""

A, B = map(int, input().split())

C = int(input())

nHour, nMin = C // 60, C % 60

hour, minute = A + nHour, B + nMin

if minute >= 60:
    minute -= 60
    hour += 1

if hour >= 24:
    hour -= 24

print(f"{hour} {minute}")
