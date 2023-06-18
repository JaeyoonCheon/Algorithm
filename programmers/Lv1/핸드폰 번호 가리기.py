"""
    lv.1 핸드폰 번호 가리기
    
    1.  슬라이싱을 사용해 풀이 가능
    2.  "\d(?=\d{4})" (후방에 길이 4의 숫자가 있는 숫자)를 사용해 검사 후 *로 대체
"""

import re


def solution(phone_number):
    answer = ""

    answer = re.sub("\d(?=\d{4})", "*", phone_number)

    return answer
