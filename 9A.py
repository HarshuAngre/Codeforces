from math import gcd

y,w = map(int,input().split())

need = max(y,w)

winning = 6 - need + 1
denominator = 6

g = gcd(winning,denominator)

print(f"{winning // g}/{denominator // g}")