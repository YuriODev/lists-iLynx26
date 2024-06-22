num = int(input())

lst = []

for i in range(num):
    lst.append(input())

max_length = 0

for element in lst:
     if len(element) > max_length:
          max_length = len(element)

list_of_indices = []

for i in range(len(lst)):
    element = lst[i]
    if len(element) == max_length:
          list_of_indices.append(str(i+1))

print("\n".join(list_of_indices))