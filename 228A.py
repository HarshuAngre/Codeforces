s = list(map(int,input().split()))

diff = set(s)

answer = 4 - len(diff)

print(answer)