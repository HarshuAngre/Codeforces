n, k, l, c, d, p, nl, np = map(int,input().split())

total_drink = (k*l) // nl
lime = c*d
salt = p // np

toast = min(total_drink,lime,salt)
answer = toast // n
print(answer)