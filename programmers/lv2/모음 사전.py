"""
    lv.2 모음 사전
    
    1.  5^5 가지수의 사전이기 때문에, 전체 사전을 생성한 뒤 인덱스를 찾는 것이 편리
"""

vowel = ["A", "E", "I", "O", "U"]
dict = []


def makeWord(word):
    dict.append(word)
    if len(word) == 5:
        return

    for c in vowel:
        makeWord(word + c)


def solution(word):
    answer = 0

    makeWord("")

    answer = dict.index(word)

    return answer
