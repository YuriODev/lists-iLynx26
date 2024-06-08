lst = list(map(int, input().split(",")))

output = []

for num in lst:
    if num % 2 == 1:
        output.append(str(num))

print(' '.join(output))