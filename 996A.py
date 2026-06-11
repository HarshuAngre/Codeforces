n = int(input())

bills = 0

bills += n // 100
n = n%100

bills += n // 20
n = n%20

bills += n // 10
n = n%10

bills += n // 5
n = n%5

bills += n // 1

print(bills)