"""
1259번 팰린드롬수

1.  팰린드롬 수이므로 짝수일때는 가운데 기준 양 쪽이 동일
    홀수일 때는 임의의 가운데 수를 제외한 양 쪽이 동일
    
2.  문자열 인덱스 슬라이싱 사용
"""


def checkPRD(number):
    numberString = list(str(number))
    length = len(numberString)

    if length % 2 == 1:
        pre = numberString[: len(numberString) // 2]
        post = numberString[len(numberString) // 2 + 1 :]
    else:
        pre = numberString[: len(numberString) // 2]
        post = numberString[len(numberString) // 2 :]

    post.reverse()

    if pre == post:
        return "yes"
    else:
        return "no"


while True:
    tc = int(input())
    if tc == 0:
        break

    print(checkPRD(tc))
