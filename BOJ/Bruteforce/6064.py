"""
6064 카잉 달력
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
    
    while xStart != x and yStart != y:
        count += 1
        xStart += 1
        yStart += 1

    if M > N:
        divisor = "right"
    else:
        divisor = "left"

    while count < maxCount:
        if xStart == x and yStart == y:
            rightAnswer = True
            break
        
        if divisor == "right":
            yStart += M
            yStart %= N
            count += M
        else:
            yStart += N
            yStart %= M
            count += N
            
        
    return count if rightAnswer else -1
        

iter = int(input())

for _ in range(iter):
    M, N, x, y = map(int, input().split())
    print(calculateFast(M, N, x, y))
    