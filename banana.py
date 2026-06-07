cost, money, bananas = map(int, input().split())

total = 0
borrow= 0
for i in range(1,bananas+1):
    sum=cost * i
    total += sum

if total > money:
    borrow = total-money

print(borrow)
