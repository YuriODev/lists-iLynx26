lst = list(map(int, input().split()))

print(f"{((lst[0]-lst[2])**2 + (lst[1] - lst[3])**2)**0.5:.2f}")