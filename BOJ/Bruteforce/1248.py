"""
1248번 맞춰봐

문제) N개의 -10 ~ 10 수열에서 만들 수 있는 N(N+1)/2개의 순열조합의 부호만 나타낸 문자열이 주어짐
이 문자열로 원래 주어진 N개의 숫자를 구하는 것

아이디어) 1. [0번째] - [N번째] - [N + (N - 1)번째] - ... - [N + (N - 1)+ 1번째] 부호는 각각 N개의 숫자의 부호와 같을 것
해당 위치의 부호는 숫자 1개일 때의 합의 부호이기 때문
"""


def findNsigns(N, signs):
    Nsigns = []
    tempIdx = 0
    tempCount = N

    for i in range(len(signs)):
        if i == tempIdx:
            Nsigns.append(signs[i])
            tempIdx += tempCount
            tempCount -= 1

    return Nsigns


def checkSigns(N, numbers, signs):
    count = 0
    for i in range(N):
        sum = 0
        for j in range(i, N):
            sum += numbers[j]
            if signs[count] == "+" and sum <= 0:
                return False
            if signs[count] == "-" and sum >= 0:
                return False
            if signs[count] == "0" and sum != 0:
                return False
            count += 1

    return True


def findNumbers(N, signs, Nsigns, numbers, length):
    global flag
    if length == N:
        if checkSigns(N, numbers, signs):
            if flag == False:
                for i in numbers:
                    print(i, end=" ")
                flag = True
    else:
        if Nsigns[length] == "+":
            for i in range(1, 11):
                numbers.append(i)
                findNumbers(N, signs, Nsigns, numbers, length + 1)
                numbers.pop()
        elif Nsigns[length] == "-":
            for i in range(-1, -11, -1):
                numbers.append(i)
                findNumbers(N, signs, Nsigns, numbers, length + 1)
                numbers.pop()
        else:
            numbers.append(0)
            findNumbers(N, signs, Nsigns, numbers, length + 1)
            numbers.pop()


N = int(input())
signs = input()
Nsigns = findNsigns(N, signs)
numbers = []
flag = False

findNumbers(N, signs, Nsigns, numbers, 0)
