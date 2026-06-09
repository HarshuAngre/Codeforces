n = int(input())
previous = input()
group = 1


for i in range(n-1):
    current = input()

    if current != previous:
        group += 1
    
    previous = current

print(group)

    