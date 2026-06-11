n = int(input())

result = []
while n <= 100:
    if n >= 90:
        result.append('A')
        n += 1
    elif 90> n >= 80:
        result.append('B')
        n += 1
    elif 80 > n >= 70:
        result.append('C')
        n += 1
    elif 70 > n >= 60:
        result.append('D')
        n += 1
    elif 60 > n:
        result.append('F')
        n += 1

print(*result)