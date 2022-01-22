num = int(input())
divisor = [int(i) for i in input().split()]

maxDivisor = max(divisor)
minDivisor = min(divisor)

print(maxDivisor * minDivisor)
