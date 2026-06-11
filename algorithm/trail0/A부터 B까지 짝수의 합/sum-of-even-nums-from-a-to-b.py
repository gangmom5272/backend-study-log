a, b = map(int, input().split())

lst = []

for i in range(a, b+1):
    if i % 2 == 0:
        lst.append(i)

print(sum(lst))