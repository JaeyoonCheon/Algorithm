"""
6064 카잉 달력

1. x, y를 하나씩 증가시키는 방법
이 방법은 정답을 찾아낼 수 있으나 시간복잡도가 O(M*N)으로 간주
시간 제한을 넘길 수 없었음

2. x, y 둘 중 하나를 고정시키고 다른 하나만 증가시켜 나누어 반복
우선, x와 y가 같아지는 지점까지 증가시킨 후, 더 작은 쪽의 최대 수로 나누어 시계 처럼
증가 후 나머지 연산을 하여 중간의 필요없는 연산을 축약
나누어 나머지가 0이 되는 지점의 예외처리가 이 코드에서는 필요(예외 없이 작성 가능할 듯)
"""

def GCD(a, b):
    if a > b:
        remainder = a % b
        return b if remainder == 0 else GCD(b, remainder)
    else:
        remainder = b % a
        return a if remainder == 0 else GCD(a, remainder)

def calculate(M, N, x, y):
    rightAnswer = False
    count = 0
    maxCount = M * N / GCD(M, N)

    xStart = 1
    yStart = 1

    while count < maxCount:
        count += 1
        if xStart == x and yStart == y:
            rightAnswer = True
            break
        xStart += 1
        yStart += 1
        if xStart > M:
            xStart = 1
        if yStart > N:
            yStart = 1

    return count if rightAnswer else -1

def calculateFast(M, N, x, y):
    divisor = ""
    rightAnswer = False
    count = 1
    maxCount = M * N / GCD(M, N)

    xStart = 1
    yStart = 1

    if M > N:
        divisor = "right"
        while yStart != y:
            count += 1
            xStart += 1
            yStart += 1
    else:
        divisor = "left"
        while xStart != x:
            count += 1
            xStart += 1
            yStart += 1
    
    while count <= maxCount:
        if xStart == x and yStart == y:
            rightAnswer = True
            break
        
        if divisor == "right":
            xStart += N
            if xStart % M == 0:
                count+=N
            else:
                xStart %= M
                count += N
        else:
            yStart += M
            if yStart % N == 0:
                count+=M
            else:
                yStart %= N
                count += M
            
        
    return count if rightAnswer else -1
        

iter = int(input())

for _ in range(iter):
    M, N, x, y = map(int, input().split())
    print(calculateFast(M, N, x, y))
    