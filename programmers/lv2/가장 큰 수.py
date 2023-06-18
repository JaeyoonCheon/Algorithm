"""
    lv.2 가장 큰 수
    
    1.  수 간에 정렬 기준을 두 수를 뽑아 앞뒤/뒤앞 결합했을 때 숫자가 더 큰 순서대로 정렬
    2.  정렬한 배열을 하나로 합치면서 앞쪽의 0을 모두 제거하고 문자열로 반환
"""

import functools


def solution(numbers):
    answer = ""

    strings = list(map(str, numbers))

    strings.sort(
        key=functools.cmp_to_key(lambda a, b: int(a + b) - int(b + a)), reverse=True
    )

    answer = str(int("".join(strings)))

    return answer
