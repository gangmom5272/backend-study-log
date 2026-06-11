result_a = []
result_b = []
arr = []

for i in range(10):
    a = int(input())
    arr.append(a)

for a in arr:
    if a % 3 == 0:
        result_a.append(a)
    
for b in arr:
    if b % 5 == 0:
        result_b.append(b)

print(len(result_a), len(result_b))