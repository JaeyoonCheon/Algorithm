"""
9012번 괄호
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
