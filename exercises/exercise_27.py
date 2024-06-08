n = int(input())

output = 0

for i in range(n):
    action = input()
    if "D" in action:
        output += int(action[1::])
    else:
        output -= int(action[1::])

print(output)