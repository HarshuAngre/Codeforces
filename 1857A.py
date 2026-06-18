t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    odd = 0

    for x in arr:
        if x % 2:
            odd += 1

    if odd % 2 == 0:
        print("YES")
    else:
        print("NO")