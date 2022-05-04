def newCheckHat(seq):
    """
    가장 앞사람의 모자 방향에 따라 그 반대 방향을 뒤집어야 할 방향으로 지정
    가장 앞사람의 모자 방향이 정해지면, 그 방향 구간의 수는 가장 끝 사람의 모자 방향에 따라
    구간의 수가 반드시 같거나 1개 더 많아진다
    따라서, 뒤집어야 하는 구간의 숫자는 가장 앞 사람의 반대 방향 구간의 수이다.
    """
    # 방향이 바뀌는 지점
    start = 0
    # 가장 첫 사람의 방향
    major = seq[0]
    # 가장 끝에 종료조건을 위하여 첫 번째 사람의 방향을 삽입(결과적으로 count되지 않음)
    seq = seq + [seq[0]]

    for i in range(1, len(seq)):
        if seq[i] != seq[i-1]:
            if seq[i] != major:
                start = i
                print("flip hat from", start, end="")
            else:
                print(" to", i-1)

def checkHat(seq):
    """
    단순 구간 분리 후 갯수가 더 적은 쪽을 flip
    """
    interval = []
    start = forward = backward = 0

    for i in range(1, len(seq)):
        if seq[i] != seq[i-1]:
            interval.append((start, i-1, seq[start]))
            if seq[start] == "F":
                forward = forward + 1
            else:
                backward = backward + 1
            start = i

    interval.append((start, len(seq)-1, seq[start]))

    if seq[start] == "F":
        forward = forward + 1
    else:
        backward = backward + 1

    if forward < backward:
        flip = "F"
    else:
        flip = "B"

    for i in interval:
        if i[2] == flip:
            print("flip from", i[0], "to", i[1])

seq1 = ["F", "F", "B", "F", "F", "F", "B", "B", "F", "F", "B", "B", "B", "B"]

checkHat(seq1)
newCheckHat(seq1)