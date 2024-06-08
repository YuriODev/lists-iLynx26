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

# number_lst = list(map(int, number_lst))
# max_number = min(number_lst)
# max_index = number_lst.index(max_number)

# if max_index == 0:
#     print(number_lst[1:])
# elif max_index == len(number_lst) - 1:
#     print(number_lst[:-1])
# else:
#     print(number_lst[:max_index] + number_lst[max_index+1:])

