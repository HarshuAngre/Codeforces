t = int(input())

cards = list(map(int,input().split()))

Serja = 0
Dima = 0
turn = 0

while(cards):
    if cards[0] > cards[-1]:
        picked = cards[0]
        cards.pop(0)
    else:
        picked = cards[-1]
        cards.pop()

    if turn % 2 == 0:
        Serja += picked
    else:
        Dima += picked

    turn += 1


print(Serja,'',Dima)
       


