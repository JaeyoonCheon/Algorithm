"""
    lv.4 호텔 방 배정

    1.  10^12개의 방에 번호를 순차적으로 검색/삽입을 해야 하는데 일반적인 리스트로는 공간/시간 부족. 따라서 딕셔너리로 인덱스만 사용해야 함
    2.  방 번호에 대해 더 큰 번호 & 빈 방인 조건을 1씩 증가하며서 찾아 삽입하는 로직 작성. 
        이 단순 로직으로는 매번 빈 방을 하나하나 찾아가야 하므로 비효율적.
    3.  기존에는 딕셔너리에 방 번호라는 키만 사용했으나, 그 값으로 해당 번호 다음으로 넣을 수 있는 빈 방을 번호를 저장해 점프할 수 있도록 유도.
        이 때, 점프하는 과정에서 방문한 모든 방의 번호의 값을 일괄적으로 업데이트해야 한다.
"""


def iter(k, room_number):
    hotel = {}

    for num in room_number:
        temp = num
        visited = []
        while True:
            if temp not in hotel:
                hotel[temp] = temp + 1
                break
            else:
                temp = hotel[temp]
                visited.append(temp)

        for room in visited:
            hotel[room] = temp + 1

    return list(hotel)


def solution(k, room_number):
    answer = iter(k, room_number)
    return answer


result = solution(10, [1, 3, 4, 1, 3, 1])
