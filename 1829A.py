t = int(input())

c = "codeforces"


for _ in range(t):
    s = input()
    counter = 0

    for i in range(10):
        if s[i] != c[i]:
            counter += 1
        
    print(counter)


    