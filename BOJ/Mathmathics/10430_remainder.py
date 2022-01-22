A, B, C = map(int, input().split())

result = []

result.append((A + B) % C)
result.append(((A % C) + (B % C)) % C)
result.append((A * B) % C)
result.append(((A % C) * (B % C)) % C)

for i in result:
    print(i)
