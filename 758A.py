n =int(input())
array = list(map(int,input().split()))

richest = max(array)

total = 0

for i in array:
    total += richest - i

print(total)
