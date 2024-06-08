lst = input().split("_")

final_list = [word.capitalize() for word in lst]

print("".join(final_list))