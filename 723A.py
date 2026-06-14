x1, x2, x3 = map(int,input().split())

maxx = max(x1,x2,x3)
least = min(x1,x2,x3)

answer = maxx - least

print(answer)