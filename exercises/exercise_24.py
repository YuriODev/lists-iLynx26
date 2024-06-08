lst = sorted(list(map(int, input().split())), reverse = True)

while 0 in lst:
    lst.remove(0)
    
print(" ".join(list(map(str, lst))))
