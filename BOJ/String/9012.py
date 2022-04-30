"""
9012번 괄호

1.  문자열 찾아서 대체하는 문제.
    "()"를 찾아서 ""으로 대체하고 없을때 까지 반복
    만약 "()"가 없는데 남아있는 문자열이 있다면 실패.
"""

T = int(input())

for _ in range(T):
    case = str(input())

    isVPS = True

    while case != "":
        if "()" in case:
            case = case.replace("()", "")
        else:
            isVPS = False
            break

    if not isVPS:
        print("NO")
    else:
        print("YES")
