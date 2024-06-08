lst = input().split() 

unique_lst = []

for num in lst:
    if num not in unique_lst:
        unique_lst.append(num)

print(len(unique_lst))