s = input()
alp = []
for i in s:
    if i.isalpha():
        alp += i


print(len(set(alp)))