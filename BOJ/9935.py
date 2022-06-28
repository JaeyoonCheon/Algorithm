"""
9935번 문자열 폭발

1.  첫 시도에서 파이썬 내장함수인 find/replace를 사용하여 답을 구할 수 있었으나
    내장 함수 자체가 중간 인덱스를 조작하는 함수로 시간복잡도가 N^2일 것이고 시간초과가 발생하였다.
"""

sentence = input()
boom = input()


def simpleMethod():
    while sentence.find(boom) != -1:
        sentence = sentence.replace(boom, "")

    if sentence == "":
        print("FRULA")
    else:
        print(sentence)
