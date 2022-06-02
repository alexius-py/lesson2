name_users = input("Введите Ваше имя: ")
print("Приветствую", name_users, "в игре Вопрос-Ответ")
two_game = "д"
while True:
    if two_game == "н":
        print("До скорой встречи", name_users)
        break
    elif two_game == "д":
        wow = 0
        loss = 0
        two_game = "None"
        print(name_users, "тебе будет задано последовательно 5 вопросов")
        print("каждый правельный ответ 1 балл")
        print("игра началась!")
        print("В каком году умер писатель знаменитой книги 'Мастер и Маргарита'?")
        # Михаил Булгаков 1891-1940
        qution1 = input("Ваш ответ: ")
        while not qution1.isdigit():
            print("Вы ввели не правлильный формат ответа, только цифры")
            qution1 = input("Ваш ответ: ")
        qution1 = int(qution1)
        if qution1 == 1940:
            wow += 1
        else:
            loss += 1
        print("В каком году А. С. Пушкин написал свое первое стихотворение?")
        # А. С.Пушкин свое первое стихотворение он написал, когда ему исполнилось 15, 1799-1837
        qution2 = input("Ваш ответ: ")
        while not qution2.isdigit():
            print("Вы ввели не правлильный формат ответа, только цифры")
            qution2 = input("Ваш ответ: ")
        qution2 = int(qution2)
        if qution2 == 1814:
            wow += 1
        else:
            loss += 1
        print("Год рождения Николая Васильевича Гоголя?")
        # Н. В. Гоголь 1809-1852
        qution3 = input("Ваш ответ: ")
        while not qution3.isdigit():
            print("Вы ввели не правлильный формат ответа, только цифры")
            qution3 = input("Ваш ответ: ")
        qution3 = int(qution3)
        if qution3 == 1809:
            wow += 1
        else:
            loss += 1
        print("Год смерти Александра Исаевича Солженицына?")
        # Александр Исаевич Солженицын 1918-2008
        qution4 = input("Ваш ответ: ")
        while not qution4.isdigit():
            print("Вы ввели не правлильный формат ответа, только цифры")
            qution4 = input("Ваш ответ: ")
        qution4 = int(qution4)
        if qution4 == 2008:
            wow += 1
        else:
            loss += 1
        print("Год рождения автора произведения 'Преступление и наказание'?")
        # Федор Михайлович Достоевский 1821-1881
        qution5 = input("Ваш ответ: ")
        while not qution5.isdigit():
            print("Вы ввели не правлильный формат ответа, только цифры")
            qution5 = input("Ваш ответ: ")
        qution5 = int(qution5)
        if qution5 == 1821:
            wow += 1
        else:
            loss += 1
        print("Правельных ответов:", wow)
        print("Неправельных ответов:", loss)
        print("Процент правельных ответов", (wow * 100) / 5)
        print("Процент неправельных ответов", (loss * 100) / 5)
        if wow == 0:
            print(name_users, "твоя оценка НЕУТ!!! (СРОЧНО В ШКОЛУ)")
        elif 1 <= wow <= 2:
            print(name_users, "твоя оценка ПЛОХО, (нужно больше читать)")
        elif wow == 3:
            print(name_users, "твоя оценка УДОВЛЕТВОРИТЕЛЬНО")
        elif wow == 4:
            print(name_users, "твоя оценка ХОРОШО!!")
        else:
            print(name_users, "твоя оценка ОТЛИЧНО!!!")
    else:
        two_game = input("Повторим д (да)/н (нет):")
