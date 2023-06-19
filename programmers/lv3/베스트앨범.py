"""
    lv.3 베스트앨범
    
    1.  조건 1과 2에서 제시하는 장르 별 총 재생 수 / 장르 내 각각의 재생 수 정보를 가지는 딕셔너리를 분리해 저장.
    2.  해당 딕셔너리들을 내림차순 정렬해 값을 가져와 반환.
"""


def solution(genres, plays):
    answer = []

    totalPlays = {}
    genreNumber = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        totalPlays[genre] = totalPlays.get(genre, 0) + play

        if genre not in genreNumber:
            genreNumber[genre] = [(i, play)]
        else:
            genreNumber[genre].append((i, play))

    sortedTotalPlays = sorted(totalPlays.items(), key=lambda x: x[1], reverse=True)

    for gen, _ in sortedTotalPlays:
        sortedGenreNumber = sorted(genreNumber[gen], key=lambda x: x[1], reverse=True)[
            :2
        ]

        for num, _ in sortedGenreNumber:
            answer.append(num)

    return answer


result = solution(
    ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
)
