"""
    lv.1 문자열 다루기 기본
    
    1.  문자열 길이 대조 & 문자열의 문자들이 모두 숫자인지 isdigit으로 확인
    2.  s의 길이가 4 또는 6인지 확인 & "^[0-9]*$" (0개 이상인 숫자로 시작하고 끝나는 문자열)로 검사
    3.  "^(\d{4}|\d{6})$" (길이 4 또는 길이 6인 숫자로 시작하고 끝나는 문자열)로 검사
"""


def solution(s):
    answer = False

    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            answer = True

    return answer


import re


def solutionRegex1(s):
    return len(s) in {4, 6} and bool(re.match("^[0-9]*$", s))


def solutionRegex2(s):
    return bool(re.match("^(\d{4}|\d{6})$", s))
