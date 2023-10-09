def naibolee_chastye_simvoly(vhodnaya_stroka):
    vhodnaya_stroka = vhodnaya_stroka.replace(" ", "") 
    chastota_simvolov = {}

    for simvol in vhodnaya_stroka:
        if simvol.isalpha():  
            chastota_simvolov[simvol] = chastota_simvolov.get(simvol, 0) + 1

    otsortirovannye_simvoly = sorted(chastota_simvolov.items(), key=lambda x: x[1], reverse=True)
    return otsortirovannye_simvoly[:3]

# Пример использования
vhodnaya_stroka = input("Введите строку: ")
naibolee_chastye = naibolee_chastye_simvoly(vhodnaya_stroka)
for simvol, kolichestvo in naibolee_chastye:
    print(f"Символ '{simvol}' встречается {kolichestvo} раз(а)")
