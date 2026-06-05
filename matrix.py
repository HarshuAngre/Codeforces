for i in range(5):
    row = list(map(int, input().split()))

    for j in range(5):
        if row[j] == 1:
            one_row = i
            one_col = j

answer = abs(one_row - 2) + abs(one_col - 2)

print(answer)