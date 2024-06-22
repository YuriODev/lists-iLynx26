lst = list(map(int, input().split()))

if len(lst) == 1:
    print(lst[0])
else:
    new_lst = [0] * len(lst)

    for i in range(len(lst)):
        if i == 0:
            new_lst[0] = lst[1] + lst[-1]
        elif i == len(lst) - 1:
            new_lst[-1] = lst[-2] + lst[0]
        else:
            new_lst[i] = lst[i-1] + lst[i+1]

    print(" ".join(list(map(str, new_lst))))
