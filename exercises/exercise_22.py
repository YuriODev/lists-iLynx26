lst = input()

sum_ = 0

for i in range(len(lst)):
    sum_ += int(lst[len(lst)-i-1])*2**i

print(sum_)