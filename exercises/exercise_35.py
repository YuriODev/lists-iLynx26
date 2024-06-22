lst = input().split()

zeros = lst.count("0")

for i in range(zeros):
    lst.remove("0")

lst += "0" * zeros

print(" ".join(lst))