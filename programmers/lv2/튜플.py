"""
    lv.2 튜플
    
    1.  문자열로 주어지는 입력값을 리스트로 파싱
    2.  파싱된 리스트를 길이 순 오름차순 정렬한 뒤, 작은 것 부터 새로 추가되는 수를 순서대로 추가

    3.  추가 - in 연산자를 사용해 중복 체크를 할 경우, 해시를 이용한 딕셔너리를 적용하여 결과값으로 반환 가능.
        딕셔너리를 리스트로 형 변환 시 초기화한 순서대로 리스트에 적용됨.
"""


def solution(s):
    answer = []
    answerDict = {}

    arrays = s[2:-2].split("},{")

    arrays.sort(key=lambda x: len(x))
    arrays = list(map(lambda x: list(map(int, x.split(","))), arrays))

    for array in arrays:
        for i in array:
            if i not in answerDict:
                answerDict[i] = True

    return list(answerDict)


solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")
