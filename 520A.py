n = int(input())
s = input()

s = s.lower()

length = len(set(s))

if length >= 26:
    print('YES')
else:
    print('NO')
