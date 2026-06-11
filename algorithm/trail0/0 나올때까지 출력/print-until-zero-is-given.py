result = []
for i in range(101):
    n = int(input())
    if n != 0:
        result.append(n)
    else:
        break
for i in range(len(result)):
    print(result[i])