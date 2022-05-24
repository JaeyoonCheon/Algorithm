"""
5525번 IOIOI

1.  주어진 긴 문장에서 원하는 길이의 IOI 패턴을 찾아 몇 개인지 세야 하는 문제로,
    문자열 인덱싱을 정확하게 해야 통과 가능하다.
    
2.  우선, N에 맞는 IOI패턴 문자열을 string에 만들어 놓고,
    문장 처음부터 해당 패턴을 찾는다면, 그 뒤에 붙어 나오는 OI 패턴을 몇 개인지 찾아
    그 수를 더해주면 인접한 패턴의 수를 셀 수 있다.
    
3.  이후 가장 끝까지 탐색한 인덱스-1을 탐색 시작위치로 설정해주고,
    시작 위치가 끝에서부터 찾으려는 패턴을 길이보다 작은 위치에 도달하게 되면
    종료하는 방식으로 구현했다.
"""


N = int(input())
M = int(input())
S = input()

count = 0

start, end = 0, 0

partialString = ["I"]
for _ in range(N):
    partialString.append("O")
    partialString.append("I")

string = "".join(partialString)

while start <= M - (2 * N + 1):
    if S[start : start + (2 * N + 1)] == string:
        end = start + (2 * N + 1)
        extension = 1
        while True:
            if S[end : end + 2] == "OI":
                extension += 1
                end += 2
            else:
                break

        count += extension
        start = end - 1
    else:
        start += 1

print(count)
