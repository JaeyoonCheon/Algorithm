"""
1874번 스택 수열

1.  스택에 n개의 수를 1부터 n까지 오름차순으로 순서대로 집어넣는다는 조건 하에,
    주어진 수열을 push/pop으로 표시 가능하냐의 문제
    
2.  스택에서 push와 pop을 할 조건을 세우면
    현재 n개의 수 중 i까지 넣었다는 가정 하에
    1)  i가 표시해야 할 수열의 수 number보다 작을 때
        i부터 number까지의 수를 순서대로 스택에 넣고 1번만 pop을 수행
    2)  i가 표시해야 할 수열의 수 number보다 클 때
        2-1)    스택이 비어있지 않으면
                2-1-1)  number가 나올 때 까지 계속 pop
                2-1-2)  나오지 않는다면 수열을 만들 수 없으므로 NO 출력 후 종료
        2-2)    스택이 비어있다면 pop이 불가능하므로 NO 출력 후 종료

3.  이상의 절차중 push/pop 시의 동작을 따로 저장 후 출력        
"""

import sys

N = int(input())

sequences = [int(input()) for _ in range(N)]
operation = []
stacks = []
current = 1

for number in sequences:
    # 스택에 넣어 number를 만들 수 있는 여유가 있는 경우
    if current < number:
        for i in range(current, number + 1):
            stacks.append(i)
            operation.append("+")
            current += 1

        stacks.pop()
        operation.append("-")
    elif current > number:
        if stacks:
            found = False
            while stacks:
                top = stacks.pop()
                operation.append("-")

                if top == number:
                    found = True
                    break
            if found == False:
                print("NO")
                sys.exit()
        else:
            print("NO")
            sys.exit()
    else:
        stacks.append(number)
        operation.append("+")
        current += 1
        stacks.pop()
        operation.append("-")

for i in operation:
    print(i)
