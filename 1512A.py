t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))

    if array[0] == array[1]:
        common = array[0]
    elif array[1] == array[2]:
        common = array[1]
    else:
        common = array[0]

    for i in range(n):
        if array[i] != common:
            index = i+1

    print(index)
        