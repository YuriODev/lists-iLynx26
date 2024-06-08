lst = list(map(int, input().split(",")))

output = []

for i in range(lst):
    if i % 2 == 0:
        output.append(str(lst[i]))

print(','.join(output))