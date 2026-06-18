t = int(input())

for _ in range(t):
    n,k = map(int,input().split())

    array = list(map(int,input().split()))

    if k > 1:
        print('YES')
    elif k == 1:
        if array == sorted(array):
            print('YES')
        else:
            print('NO')