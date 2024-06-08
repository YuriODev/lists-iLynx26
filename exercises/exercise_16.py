lst = input().split()

new_lst = []

for num in lst:
    if lst.count(num) == 1:
        new_lst.append(num)

print(" ".join(new_lst))