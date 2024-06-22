lst = input().split()
num = input()

if num not in lst:
    print(None)
else:
    indexes = []
    for i in range(lst.count(num)):
        index = lst.index(num)
        indexes.append(str(index+1))
        lst[index] = "*"

    print(" ".join(indexes))