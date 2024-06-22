lst = input().split()

max_length = 0

for word in lst:
    if len(word) > max_length:
        max_length = len(word)

num_lst = []

for word in lst:
    if len(word) == max_length:
        num_lst.append(word)

print(" ".join(num_lst))