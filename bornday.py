year = int(input("Введите год рождения А. С. Пушкина: "))
if year == 1799:
    date = int(input("Введите день рождение: "))
    if date == 26:
        print("Верно")
    else:
        print("Неверный день рождения")
else:
    print('Неверно')