import sys

"""
1248번 맞춰봐

문제) N개의 -10 ~ 10 수열에서 만들 수 있는 N(N+1)/2개의 순열조합의 부호만 나타낸 문자열이 주어짐
이 문자열로 원래 주어진 N개의 숫자를 구하는 것

아이디어) 1. [0번째] - [N번째] - [N + (N - 1)번째] - ... - [N + (N - 1)+ 1번째] 부호는 각각 N개의 숫자의 부호와 같을 것
해당 위치의 부호는 숫자 1개일 때의 합의 부호이기 때문

조건) 각 N개의 숫자는 중복된 숫자를 불허한다는 말이 없고, 순서에 따라 결과값이 바뀔 것이므로, 중복순열을 구성해야 한다.

해결) 위 아이디어를 기초로 문제에 나온 S[i][j]에 맞추어 처음 입력받는 부호 문자열을 2차원 배열로 간주하였다.
이 때, S[M][M]은 각각의 N개의 숫자의 부호와 동일하다. 그리고 대각 성분의 위쪽 열 성분에 위치한 원소들은 
해당 숫자부터 원소의 행 index까지의 숫자의 합의 부호이다. (예> S[M][N] = X_M + ~ + X_N의 부호)
따라서, N개의 숫자를 -10 ~ 10 범위 내에서 백트래킹으로 테스트해보면서 각 자리에 숫자가 들어가 부호 조건을 만족시킬 수 있는 지 검사하면 된다.
이 경우, 부호의 검사는 열 단위로 이루어지므로 순서대로 재귀 깊이를 구성할 수 있다.
"""


"""
시간 초과
재귀 깊이가 너무 깊어져 1초 제한시간 내에 동작이 안되는 것으로 생각됨
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
"""


def checkSign(sign, numbers, length):
    sum = 0

    for i in range(length, -1, -1):
        sum += numbers[i]

        if sign[i][length] == "+" and sum <= 0:
            return False
        if sign[i][length] == "-" and sum >= 0:
            return False
        if sign[i][length] == "0" and sum != 0:
            return False

    return True


def findNumbers(N, sign, numbers, length):
    if length == N:
        for i in numbers:
            print(i, end=" ")
        sys.exit()

    for i in range(-10, 11):
        numbers.append(i)
        if checkSign(sign, numbers, length) == True:
            findNumbers(N, sign, numbers, length + 1)
        numbers.pop()


N = int(input())
temp = input()
sign = []
count = 0
for i in range(N, 0, -1):
    tempString = ""
    for j in range(N - i):
        tempString += " "
    slices = slice(count, count + i)
    tempString += temp[slices]
    sign.append(tempString)
    count += i
numbers = []
flag = False

findNumbers(N, sign, numbers, 0)
