lst = list(map(int, input().split()))

greater_then_neighbours = 0

for i in range(1, len(lst)-1):
    num = lst[i]
    if lst[i] != -1:
        if num > lst[i-1] and num > lst[i+1]:
            greater_then_neighbours += 1
    else:
        break

print(greater_then_neighbours)