"""
1436번 영화감독 숌

1.  단순 수에서 "666"이 포함된 것을 계산하기에는 번거로우므로,
    수를 문자열로 변환하여 substring "666"이 포함되어 있는 지 확인
"""

N = int(input())

count = 0
num = 666

while count != N:
    if str(num).find("666") != -1:
        count += 1
    num += 1

print(num - 1)
