n = int(input())
emojis = list(input())

new_emojis = ""

unicode_str_start = int('1F600', 16)
unicode_str_finish = int('1F64F', 16)

emojis_list = [chr(unicode_str) for unicode_str in range(unicode_str_start, unicode_str_finish)]

new_emojis = ""
for emoji in emojis:
    new_emojis += emojis_list[emojis_list.index(emoji) + n]

print(new_emojis)
