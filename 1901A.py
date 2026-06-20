t = int(input())

for _ in range(t):
    n,x = map(int,input().split())
    stations = list(map(int,input().split()))


    current_max = stations[0]
    for i in range(n-1):
        current_max = max(current_max,stations[i+1]-stations[i])

    current_max = max(current_max, 2 * (x - stations[-1]))
    print(current_max)

