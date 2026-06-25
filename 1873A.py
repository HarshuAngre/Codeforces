t = int(input())

for _ in range(t):
    s = input()

    if s == "abc":
        print('YES')
    elif s[1] + s[0] + s[2] == "abc":
        print('YES')
    elif s[2] + s[1] + s[0] == "abc":
        print('YES')
    elif s[0] + s[2] + s[1] == "abc":
        print('YES')
    else:
        print('NO')
 