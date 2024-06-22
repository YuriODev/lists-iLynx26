string = input()

new_list = []

for i in range(len(string)):
    symbol = string[i]
    if symbol.isdigit():
        if string[i+1].isdigit():
            if string[i+2].isdigit():
                lst = string[i+3] * (int(symbol)*100 + int(string[i+2]) * 10 + int(string[i+1])-1)
                new_list.append(lst)
                i += 3
            else:
                lst = string[i+2]*(int(symbol)*10 + int(string[i+1])-1)
                new_list.append(lst)
                i += 2
        else:
            lst = string[i+1]*(int(symbol)-1)
            new_list.append(lst)
            i += 1
    else:
        new_list.append(symbol)

print("".join(new_list))