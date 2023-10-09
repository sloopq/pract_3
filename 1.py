def new_stroka(input_str):
    new = ""
    count = 1

    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            new += input_str[i - 1] + (str(count) if count > 1 else "")
            count = 1

    new += input_str[-1] + (str(count) if count > 1 else "")

    return new


input_str = input("Введите строку: ")
result = new_stroka(input_str)
print(result)
