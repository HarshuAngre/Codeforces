m, n = map(int, input().split())
squares = m * n
domino = 2

if squares % 2 != 0:
    squares = (squares - 1) / domino
else:
    squares = squares / domino

print(int(squares))