year = ''
while not year.isdigit():
    year = input("Введите год рождения А. С. Пушкина: ")
year = int(year)
while year != 1799:
    print("Неверно указан год")
    year = int(input("Введите год рождения А. С. Пушкина: "))
print("Верно")
