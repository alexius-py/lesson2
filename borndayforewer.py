year = ''
day = ''
while not year.isdigit():
    year = input("Введите год рождения А. С. Пушкина: ")
year = int(year)
while year != 1799:
    print("Неверно указан год")
    year = int(input("Введите год рождения А. С. Пушкина: "))
while not day.isdigit():
    day = input("Введите день рождения А. С. Пушкина: ")
day = int(day)
while day != 26:
    print("Неверно указан день")
    day = int(input("Введите день рождения А. С. Пушкина: "))
print("Верно")