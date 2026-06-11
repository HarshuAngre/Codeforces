n = int(input())
heights = list(map(int,input().split()))

max_height = max(heights)
min_height = min(heights)

for i in range(n):
    if heights[i] == max_height:
        leftindex = i
        break
    
for i in range(n-1,-1,-1):
    if heights[i] == min_height:
        rightindex = i
        break

moves = leftindex + (n-1) - rightindex



if leftindex > rightindex:
    moves -= 1

print(moves)
