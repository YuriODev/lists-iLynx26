number = list(input())

max_number = sorted(number, reverse = True)

min_number = sorted(number)

if "0" in min_number:
    count_zeros = min_number.count("0")
    first_element = min_number[count_zeros]
    min_number = first_element + "0" * count_zeros + "".join(min_number[count_zeros+1:])

print("".join(min_number) + " " + "".join(max_number))