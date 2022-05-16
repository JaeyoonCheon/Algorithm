"""
1541번 잃어버린 괄호

1.  수식에 임의로 괄호를 쳐 가장 최소가 되는 값을 만드는 문제.

2.  처음 고려한 풀이 방법은 항 마다 괄호를 쳐 보고 모든 경우의 수를 탐색해 보는 것이었다.
    식의 길이가 50보다 작거나 같고 숫자/부호로 나누면 25가지이기 때문에 해볼만 하다고 생각은 된다.
    
3.  쉽게 풀이하는 방법으로, +끼리 엮인 숫자들을 모두 더해 식에 -만 남게 만든 후,
    그 식을 계산하면 뺄셈의 차가 가장 커지므로 식의 최소값이 나오게 된다.
    
4.  주어지는 테스트케이스에 -가 없는 경우, 수 앞에 0이 붙은 경우는 자연스럽게 처리되지만,
    연산자가 없고 수 하나만 있는 경우를 별도 예외처리 해주어야 한다.
"""


def makeMin(numbers, op):
    idx = 0

    if not op:
        return numbers[0]

    while True:
        if op[idx] == "+":
            num1 = numbers.pop(idx)
            num2 = numbers.pop(idx)
            op.pop(idx)

            numbers.insert(idx, num1 + num2)
        else:
            idx += 1

        if not "+" in op:
            break

    while op:
        num1 = numbers.pop(0)
        num2 = numbers.pop(0)
        op.pop(0)

        numbers.insert(0, num1 - num2)

    return numbers[0]


exp = input()

numbers = []
op = []
num = ""

for spell in exp:
    if spell == "+" or spell == "-":
        numbers.append(int(num))
        num = ""
        op.append(spell)
    else:
        num += spell

if num:
    numbers.append(int(num))

print(makeMin(numbers, op))
