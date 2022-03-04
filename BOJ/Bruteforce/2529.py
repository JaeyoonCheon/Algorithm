"""
2529번 부등호

1. K개 만큼 부등호 기호 리스트에 입력받음
2. 재귀 백트래킹을 이용하여 모든 경우를 탐색
3. 부등호 갯수보다 숫자가 1개 더 많으므로, length + 1인 경우에 수열이 완성되었다고 간주하는 종료조건 설정
4. 매 재귀 시 마다 0~9 사이의 숫자를 1)중복 없이 2)수열에 1개 이상의 수가 존재할 경우 이전 숫자와 비교하여 조건에 따라
수를 삽입하는 백트래킹을 구성
"""


def findAnswer(K, symbols, numbers, length):
    global count
    global numbersList

    if length == K + 1:
        count += 1
        result = "".join(str(s) for s in numbers)
        numbersList.append(result)
        return
    else:
        for i in range(10):
            if i in numbers:
                continue
            if length > 0:
                if symbols[length - 1] == ">":
                    if numbers[length - 1] > i:
                        numbers.append(i)
                        findAnswer(K, symbols, numbers, length + 1)
                        numbers.pop()
                    else:
                        continue
                else:
                    if numbers[length - 1] < i:
                        numbers.append(i)
                        findAnswer(K, symbols, numbers, length + 1)
                        numbers.pop()
                    else:
                        continue
            else:
                numbers.append(i)
                findAnswer(K, symbols, numbers, length + 1)
                numbers.pop()


K = int(input())
symbols = input().split()
numbers = []
numbersList = []
count = 0

findAnswer(K, symbols, numbers, 0)

maxIdx = numbersList.index(max(numbersList))
minIdx = numbersList.index(min(numbersList))

print(numbersList[maxIdx])
print(numbersList[minIdx])
