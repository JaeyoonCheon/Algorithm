def solution(commands):
    answer = []

    table = [[i, False] for i in range(2500)]

    def find(v):
        nonlocal table
        if table[v][0] == v:
            return v
        table[v][0] = find(table[v][0])
        return table[v][0]

    def union(a, b):
        nonlocal table
        a = find(a)
        b = find(b)

        if a != b:
            table[b][0] = a

    for command in commands:
        op = command.split()

        if op[0] == "UPDATE":
            if len(op) == 4:
                r, c = int(op[1]), int(op[2])
                path = (r - 1) * 50 + (c - 1)

                table[find(path)][1] = op[3]
                # 부모 갱신!
            else:
                for cell in table:
                    if cell[1] == op[1]:
                        cell[1] = op[2]
        elif op[0] == "MERGE":
            r1, c1, r2, c2 = int(op[1]), int(op[2]), int(op[3]), int(op[4])
            path1 = (r1 - 1) * 50 + (c1 - 1)
            path2 = (r2 - 1) * 50 + (c2 - 1)

            union(path1, path2)
        elif op[0] == "UNMERGE":
            r, c = int(op[1]), int(op[2])
            path = (r - 1) * 50 + (c - 1)

            root = find(path)
            originalData = table[root][1]

            for idx, cell in enumerate(table):
                table[idx][0] = find(table[idx][0])

            for idx, cell in enumerate(table):
                if table[idx][0] == root:
                    table[idx] = [idx, False]

            table[path][1] = originalData
        else:
            r, c = int(op[1]), int(op[2])
            path = (r - 1) * 50 + (c - 1)

            val = table[find(path)][1]

            if val:
                answer.append(val)
            else:
                answer.append("EMPTY")
    return answer


commands1 = [
    "UPDATE 1 1 menu",
    "UPDATE 1 2 category",
    "UPDATE 2 1 bibimbap",
    "UPDATE 2 2 korean",
    "UPDATE 2 3 rice",
    "UPDATE 3 1 ramyeon",
    "UPDATE 3 2 korean",
    "UPDATE 3 3 noodle",
    "UPDATE 3 4 instant",
    "UPDATE 4 1 pasta",
    "UPDATE 4 2 italian",
    "UPDATE 4 3 noodle",
    "MERGE 1 2 1 3",
    "MERGE 1 3 1 4",
    "UPDATE korean hansik",
    "UPDATE 1 3 group",
    "UNMERGE 1 4",
    "PRINT 1 3",
    "PRINT 1 4",
]

commands2 = [
    "UPDATE 1 1 a",
    "UPDATE 1 2 b",
    "UPDATE 2 1 c",
    "UPDATE 2 2 d",
    "MERGE 1 1 1 2",
    "MERGE 2 2 2 1",
    "MERGE 2 1 1 1",
    "PRINT 1 1",
    "UNMERGE 2 2",
    "PRINT 1 1",
]

print(solution(commands1))
