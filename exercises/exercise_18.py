lst = list(map(int, input().split()))

min_value = min(lst)
min_index = lst.index(min_value)

max_value = max(lst)
max_index = lst.index(max_value)

lst[min_index] = max_value
lst[max_index] = min_value

print(" ".join(map(str, lst)))