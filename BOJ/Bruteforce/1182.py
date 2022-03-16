"""
1182번 부분수열의 합

1. 부분수열 : 수열 중 N개를 뽑아 중복을 허용하지 않고 만들 수 있는 수열

2. dfs + 메모이제이션으로 뽑은 위치는 제외시키고 만든 수열의 합과 S를 대조하여 수를 카운트.

3. 재귀 마다 뽑을 범위는 이전에 뽑았던 수 다음부터 뽑도록 작성함.
순서가 중복되어 결과값이 나올 수 있기 때문에
"""


def findSeq(N, S, numbers, seq, visited, last):
    global count
    length = len(seq)
    if length > N:
        return
    for i in range(last, N):
        if visited[i] == False:
            visited[i] = True
            seq.append(numbers[i])

            total = sum(seq)

            if total == S:
                count += 1

            findSeq(N, S, numbers, seq, visited, i + 1)

            seq.pop()

            visited[i] = False
        else:
            continue


N, S = map(int, input().split())

numbers = [i for i in map(int, input().split())]
seq = []
visited = [False for _ in range(N)]
count = 0

findSeq(N, S, numbers, seq, visited, 0)

print(count)
