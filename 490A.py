n = int(input())
skills = list(map(int,input().split()))

programmer = []
math = []
sportsmen = []

for i in range(n):
    if skills[i] == 1:
        programmer.append(i+1)
    elif skills[i] == 2:
        math.append(i+1)
    else:
        sportsmen.append(i+1)

teams = min(len(programmer),len(math),len(sportsmen))

print(teams)

for i in range(teams):
    print(programmer[i],math[i],sportsmen[i])    