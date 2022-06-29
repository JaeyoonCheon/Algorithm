"""
9935번 문자열 폭발

1.  첫 시도에서 파이썬 내장함수인 find/replace를 사용하여 답을 구할 수 있었으나
    내장 함수 자체가 중간 인덱스를 조작하는 함수로 시간복잡도가 N^2일 것이고 시간초과가 발생하였다.
    
2.  문자열을 순차적으로 조작하기 위해 입/출력이 O(N)인 자료구조를 사용해야 하고,
    순서를 읽을 때 뒤집히는 큐 보다는 스택이 알맞은 문제.
"""

sentence = input().rstrip()
boom = input().rstrip()


def simpleMethod():
    while sentence.find(boom) != -1:
        sentence = sentence.replace(boom, "")

    if sentence == "":
        print("FRULA")
    else:
        print(sentence)


def stackMethod():
    stack = []

    for letter in sentence:
        stack.append(letter)
        if letter == boom[-1] and "".join(stack[-len(boom) :]) == boom:
            for _ in range(len(boom)):
                stack.pop()

    result = "".join(stack)
    if result == "":
        print("FRULA")
    else:
        print(result)


stackMethod()
