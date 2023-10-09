def new_str(old_str):
    new = ""
    i = 0

    while i < len(old_str):
        char = old_str[i]
        count = ""
        i += 1

        while i < len(old_str) and old_str[i].isdigit():
            count += old_str[i]
            i += 1

        count = int(count) if count else 1
        new += char * count

    return new


old_str = input("Введите сжатую строку: ")
result = new_str(old_str)
print(result)
