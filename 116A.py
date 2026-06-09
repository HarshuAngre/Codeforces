stops = int(input())

current = 0
maximum = 0

for i in range(stops):
    a,b = map(int,input().split())
    current = current - a
    current = current + b
    
    if current > maximum:
        maximum = current

print(maximum)