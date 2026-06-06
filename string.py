n = input()
m = input()

n = n.lower()
m = m.lower()

if n < m:
    print(-1)
elif n > m:
    print(1)
else:
    print(0)
