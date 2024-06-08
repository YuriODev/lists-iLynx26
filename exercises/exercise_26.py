lst = list(map(int, input().split()))

even_nums = []
odd_nums = []

for num in lst:
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)

print(" ".join(list(map(str, sorted(even_nums, reverse=True)+sorted(odd_nums)))))