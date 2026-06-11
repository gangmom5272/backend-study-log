a, b = map(int, input().split())

result = []
result.append(a)

while a < b:
    if a % 2 != 0:
        a *= 2
        if a <= b:
            result.append(a)
    else:
        a += 3
        if a <= b:
            result.append(a)



print(*result)