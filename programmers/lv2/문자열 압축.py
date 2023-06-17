"""
    lv.2 문자열 압축
    
    1.  모든 가능한 길이/조합에 대해 검사하여 대조(1000자 길이)
"""


def solution(s):
    answer = len(s)

    # 길이 별 체크 (1부터 반까지)
    for l in range(1, len(s) // 2 + 1):
        # 현재 길이에서 최종 압축 길이
        totalLen = 0
        # 현재 길이만큼 반복되어 제거되는 개수
        tokenIter = 1
        # 현재 비교하고 있는 문자열
        token = ""

        # 처음부터 끝까지 현재 길이 간격으로 검사
        for idx in range(0, len(s) + 1, l):
            # 검사할 문자열
            temp = s[idx : idx + l]

            # 중복인 경우 개수+1, 다음 인덱스로
            if temp == token:
                tokenIter += 1
            # 중복이 아니라면 현재 단위 는 길이에 추가
            else:
                # 현재 길이만큼 최종 길이에 추가
                totalLen += len(temp)

                # 중복 카운트만큼의 숫자의 문자 길이도 최종 길이에 추가
                if tokenIter > 1:
                    totalLen += len(str(tokenIter))

                # 다시 카운트 1로 초기화
                tokenIter = 1
                # 검사할 문자열을 현재 비교 문자열로
                token = temp

        answer = min(answer, totalLen)

    return answer


result = solution("abcabcabcabcdededededede")
print(result)
