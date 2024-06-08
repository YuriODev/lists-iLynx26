# from pprint import pprint

n = int(input())
emojis = list(input())

new_emojis = ""

unicode_str_start = int('1F600', 16)
unicode_str_finish = int('1F64F', 16)

emojis_list = [chr(unicode_str) for unicode_str in range(unicode_str_start, unicode_str_finish)]
emojis_dict = {idx: emoji for idx, emoji in enumerate(emojis_list)}

# pprint(emojis_dict)

new_emojis = ""

# print(f"{len(emojis_list) = }")

# while n // len(emojis_list) >= 1:
#     n -= len(emojis_list)


for emoji in emojis:
    # print("Current emoji")
    # print(f"{emoji} - {emojis_list.index(emoji)}")
    idx = emojis_list.index(emoji) + n % len(emojis_list)
    if n < 0:
        idx += 1
    new_emojis += emojis_list[idx]
    # print(f"{emojis_list[emojis_list.index(emoji) + n % len(emojis_list)]} - {emojis_list.index(emoji) + n % len(emojis_list) + 1}")
    # print()

print(new_emojis)

