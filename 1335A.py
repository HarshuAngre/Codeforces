
t = int(input())

for i in range(t):
    n = int(input())
    if n == 3 or n == 4:
        print(1)
    else:
        answer = (n-1) // 2
        print(answer)

