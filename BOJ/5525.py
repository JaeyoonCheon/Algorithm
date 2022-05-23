"""
5525번 IOIOI
"""


N = int(input())
M = int(input())
S = input()

count = 0

start, end = 0, 0

while start < M - 3:
    if S[start : start + 3] == "IOI":
        end = start + 3
        while True:
            if S[end : end + 2] == "OI":
                end += 2
            else:
                break
        count += 1
        start = end
    else:
        start += 1

print(count)
