word_lst = ["apple", "banana", "grape", "blueberry", "orange"]
n = input()
result = []

for word in word_lst:
    if word[2] == n:
        if word not in result:
            result.append(word)
    elif word[3] == n:
        if word not in result:
            result.append(word)
   

for i in range(len(result)):
    print(result[i])
print(len(result))