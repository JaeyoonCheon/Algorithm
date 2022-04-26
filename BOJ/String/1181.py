"""
1181번 단어 정렬
"""

N = int(input())

words = [[] for _ in range(51)]

for _ in range(N):
    word = input()
    length = len(word)

    if word in words[length]:
        continue
    words[length].append(word)

for i in words:
    i.sort()

for i in range(51):
    if len(words[i]) != 0:
        for j in words[i]:
            print(j)
