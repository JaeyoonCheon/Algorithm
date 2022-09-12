"""
9527번 1의 개수 세기

1.  f(x) = x로 주어지는 문제의 함수를 잘 살펴보면 어떤 수 x에 대해 이진수로 표현했을 때
    1부터 x까지 수에서 포함된 1의 개수를 결과로 받는다. 따라서 A, B 사이(A, B 또한 포함)의 수들의 1의 개수는
    f(B)-f(A-1)이 된다.
    
2.  어떤 수 x를 이진수로 바꿔 1부터 x까지 그 1의 개수를 세는 것은 단순하게 생각한다면 쉬울 수도 있으나,
    x의 가능한 범위가 1~10^16이다. 단순 반복 계산이라도 하나하나 1을 센다면 시간이 많이 걸릴것이다.
    따라서, 반복된 구간에 대해 미리 계산해 놓고 반복을 제거하는 것이 중요하다.
    
3.  일단 수를 0부터 x까지 2진수 비트로 적어보면 규칙성을 발견할 수 있다.
    예를 들어, 0~1은 00~11에서 2번 반복되고, 00~11은 000~111에서 동일하게 2번씩 반복되는 것을 볼 수 있으며,
    반복되는 구간에서 1의 개수 accSum[x]는 2**(x-1)+2*accSum[x-1]으로 규칙을 적어서 찾아낼 수 있다.
    
4.  3에서 비트 길이에 대해 1의 개수의 누적합을 찾아낸 후 반복 구간을 구해놓은 반복합을 이용해 제거하면서 f(x)를 찾는다.
    x를 이진수로 표현했을 때, 가장 큰 비트는 x보다 크지않은 가장 큰 2의 거듭제곱수까지 1이 된다.
    또한, 해당 2의 거듭제곱수 이하부터는 x보다 비트가 1 작은 수들이 모두 나오게 되고, 이것은 이미 구해놓은 누적합에서 얻을 수 있다.
    따라서, 가장 큰 크지않은 2의 거듭제곱수 ~ x까지의 수에서 가장 큰 비트를 제외한 부분이 다시 남게 되는데
    이 부분은 방금 위에서 구한 비트 1 작은 부분에서 0~해당 길이까지의 부분을 다시 반복해 얻을 수 있다.
"""

A, B = map(int, input().split())

accSum = [0] * 64

for i in range(1, 64):
    accSum[i] = 2 ** (i - 1) + 2 * accSum[i - 1]


def f(num):
    countOne = 0
    bit = bin(num)[2:]
    bitLength = len(bit)

    for i in range(bitLength):
        if bit[i] == "1":
            lower_power = bitLength - i - 1

            countOne += accSum[lower_power]
            countOne += num - 2**lower_power + 1

            num = num - 2**lower_power

    return countOne


print(f(B) - f(A - 1))

"""
A, B = map(int, input().split())

accSum = [0] * (B + 1)


def findOne(num):
    seq = bin(num)

    return seq.count("1")


for i in range(1, B + 1):
    accSum[i] = accSum[i - 1] + findOne(i)

print(accSum[B] - accSum[A - 1])
"""
