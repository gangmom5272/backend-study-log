n = int(input())

a = 0
cnt = 0
for i in range(1, 101):
    if a < n:
        a += i
        cnt +=1
    else:
        break
print(cnt)