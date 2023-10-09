def chislo_v_slova(chislo):
   
    edinicy = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    desyatki = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    sotni = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    tysiachi = ["", "тысяча"]

    if chislo == 0:
        return "ноль"
    
    if chislo < 0 or chislo > 1000:
        return "Число должно быть в диапазоне от 1 до 1000"

    if chislo <= 9:
        return edinicy[chislo]
    
    if 10 <= chislo <= 19:
        return desyatki[chislo - 10]
    
    if chislo <= 99:
        return desyatki[chislo // 10] + (" " + edinicy[chislo % 10] if chislo % 10 != 0 else "")
    
    if chislo <= 999:
        return sotni[chislo // 100] + (" " + chislo_v_slova(chislo % 100) if chislo % 100 != 0 else "")
    
    if chislo == 1000:
        return tysiachi[1]


chislo = int(input("Введите число от 1 до 1000: "))
chislo_slovami = chislo_v_slova(chislo)
print(chislo_slovami)
