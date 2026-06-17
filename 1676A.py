t = int(input())

for _ in range(t):
    n = input()

    
    sum_first = int(n[0]) + int(n[1]) + int(n[2])
    sum_second = int(n[3]) + int(n[4]) + int(n[5])

    if sum_first == sum_second:
        print('YES')
    else:
        print('NO')
    