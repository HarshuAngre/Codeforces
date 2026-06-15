n , k = map(int,input().split())

time_left = 240 - k
total_time = 0
count = 0 

for i in range(1,n+1):
    problem_time = 5*i
    
    if total_time + problem_time <= time_left:
        total_time += problem_time
        count += 1
    else:
        break

print(count)
