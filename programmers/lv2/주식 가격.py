"""
    lv.2 주식 가격
    
    1.  단순 풀이로, 모든 n개 가격에 대해 뒤쪽의 m개를 순회하면서 큰 숫자가 있는 지 비교하여 풀이 가능.
    2.  더 효율적으로 풀이하려면 스택에 숫자의 인덱스를 넣어가면서 작아지는 숫자가 나올 경우 뽑아 바로 반영하도록 작성.
"""


def solution(prices):
    answer = [0] * len(prices)

    stack = []

    for i, p in enumerate(prices):
        # 스택 top에 더 높은 가격이 있다 = 스택 top의 오름차순은 여기까지
        while stack and prices[stack[-1]] > p:
            pos = stack.pop()
            # top의 연속된 인덱스를 계산해 저장
            answer[pos] = i - pos

        # 비교를 위해 스택에 push
        stack.append(i)

    # 모든 비교에서 남은 스택의 아이템들은 끝까지 오름차순인 경우이다.
    for i in stack:
        answer[i] = len(prices) - 1 - i

    return answer
