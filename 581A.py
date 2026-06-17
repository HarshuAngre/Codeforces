a,b = map(int,input().split())

different = min(a,b)

remaining = max(a,b) - different

same = remaining // 2

print(different,same)