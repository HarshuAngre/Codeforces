t = int(input())

for _ in range(t):
    n = input()

    parts = []

    for i in range(len(n)):
        if n[i] != '0':
            parts.append(n[i] + '0' * (len(n)-i-1))
        
print(len(parts))
print(*parts)