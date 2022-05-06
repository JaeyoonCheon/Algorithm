"""
4949번 균형잡힌 세상

1.  주어진 문자열을 순회하면서 괄호 왼쪽이 나타나면 스택에 넣고,
    괄호 오른쪽이 나타나면 스택 top과 비교한다.
    top이 짝이 맞는 괄호가 아니라면 바로 loop를 탈출하여 실패 출력
    
2.  문자열 처리와 스택 순서 등의 예외 처리를 신경써서 해 주어야 함
"""


while True:
    line = input()
    line = line[:-1]

    if not line:
        break

    stack = []
    isBalanced = True

    for i in range(len(line)):
        if line[i] == "(" or line[i] == "[":
            stack.append(line[i])
        elif line[i] == ")":
            if stack:
                top = stack.pop()
                if top != "(":
                    isBalanced = False
                    break
            else:
                isBalanced = False
                break
        elif line[i] == "]":
            if stack:
                top = stack.pop()
                if top != "[":
                    isBalanced = False
                    break
            else:
                isBalanced = False
                break
        else:
            continue

    if not stack and isBalanced:
        print("yes")
    else:
        print("no")
