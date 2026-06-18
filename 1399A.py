t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))

    array.sort()

    possible = True

    for i in range(n-1):
        if array[i+1] - array[i] > 1:
            possible = False
            break

    if possible:
        print('YES')
    else:
        print('NO')
