number = input()
number_lst = list(number)

max_number = 0

for i in range(len(number_lst)):
    new_lst = []
    for j in range(len(number_lst)):
        if i!=j:
            new_lst += number_lst[j]
    new_number = int(''.join(new_lst))
    if new_number > max_number:
        max_number = new_number

print(max_number)