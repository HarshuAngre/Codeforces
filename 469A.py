n = int(input())

x = list(map(int,input().split()))
y = list(map(int,input().split()))

xpass = x[1::]
ypass = y[1::]

passed = xpass + ypass

if n == len(set(passed)):
    print('I become the guy.')
else:
    print('Oh, my keyboard!')