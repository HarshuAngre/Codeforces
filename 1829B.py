t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))
    current = 0
    maximum = 0

    for i in array:
        if i == 0:
            current += 1
            maximum = max(maximum,current)
        elif i == 1:
            current = 0
    print(maximum)



