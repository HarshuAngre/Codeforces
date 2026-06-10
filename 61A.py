n = input()
m = input()

answer = ""

for i in range(len(n)):
    if n[i] == m[i]:
        answer += "0"
    else:
        answer += "1"

print(answer)