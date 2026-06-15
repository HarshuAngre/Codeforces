k , r = map(int,input().split())

count = 1

while True:
    total = k * count

    if total % 10 == 0 or total % 10 == r:
        print(count)
        break
    count += 1

    