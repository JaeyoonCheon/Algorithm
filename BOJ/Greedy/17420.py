"""
17420번 깊콘이 넘쳐흘러

1.  어떤 기프티콘을 해당 계획일에 쓸 수 있는 경우는 해당 날짜가 되었을 때, 해당 계획일에 사용할 기프티콘 이외의 모든 기프티콘의 만료일보다
    해당 기프티콘의 만료일이 짧아야만 한다.
2.  따라서 연장하는 시점은 다음 2가지이다.
    1)  다음 번에 당장 사용할 기프티콘이 아닌데 다음 계획일보다 만료일이 짧은 경우.
        이 경우 다음 계획일에 사용 예정인 모든 기프티콘의 만료일보다 길게 연장해야 함.
    2)  다음 번에 당장 사용할 기프티콘이 다음 계획일보다 만료일이 짧은 경우.
        이 경우 다음 계획일보다만 기간이 같거나 길도록 연장.
3.  2번의 과정을 계속 반복하면서 모든 기프티콘이 사용되어 배열이 빌 때까지 동작하도록 설계.
    이 때, 기프티콘을 사용하는 시점에서 사용하지 않을 기프티콘들을 2-1과 같이 연장을 해 주어야 해당 사용 계획일에 모든 해당하는 기프티콘들을 사용가능하다.
4.  상기 방법은 그리디 식으로 loop를 2번 돌면서 체크하므로 100000개 범위에서는 시간이 오래 걸릴것이다.
    따라서, 처음에 오름차순으로 더 작은 만료일/계획일 기준으로 정렬한 뒤 해당 날짜들을 기준으로 아래에서부터 고정된 값을 수정해 나가면
    전체 loop를 1번만 돌고 수행 가능할 것으로 생각된다.
"""

import sys
import math

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

extend = 0

while B:
    minExpire = min(A)
    deadline = min(B)
    nextGifticons = []

    for i, x in enumerate(A):
        if B[i] == deadline:
            nextGifticons.append(A[i])

    nextMaxExpire = max(nextGifticons)

    # 기한 전
    if minExpire < deadline:
        for idx, gifticon in enumerate(A):
            # 해당되는 기프티콘들에 대해
            if gifticon < deadline:
                # 다음에 바로 써야하는 기프티콘인 경우 데드라인만 넘기도록 연장
                if B[idx] == deadline:
                    count = math.ceil((deadline - gifticon) / 30)
                    extend += count
                    A[idx] += count * 30
                # 바로 쓰지 않아도 되는 기프티콘은 바로 써야하는 기프티콘을 쓸 수 있도록 해당 기프티콘의 남은 기한보다 커지게 연장
                if B[idx] > deadline:
                    count = math.ceil((nextMaxExpire - gifticon) / 30)
                    extend += count
                    A[idx] += count * 30
    # 기한이 된 경우
    else:
        for idx, gifticon in enumerate(A):
            # 해당되는 기프티콘들에 대해
            if gifticon < nextMaxExpire:
                # 바로 쓰지 않아도 되는 기프티콘은 바로 써야하는 기프티콘을 쓸 수 있도록 해당 기프티콘의 남은 기한보다 커지게 연장
                if B[idx] > deadline:
                    count = math.ceil((nextMaxExpire - gifticon) / 30)
                    extend += count
                    A[idx] += count * 30
        A = [x for i, x in enumerate(A) if B[i] != deadline]
        B = [x for x in B if x != deadline]

print(extend)
