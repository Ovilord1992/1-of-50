import random
lang = input('Choose a language/ Выберите язык en/ru:\n')
if lang == 'ru':
    summ = 0 #задаем счетчик
    attemp = 6 #задаем количество попыток
    print('Условия игры: \n 1)У вас есть 6 попыток чтобы угадать число \n 2)Числа загадываются от 1 до 50') #условия игры
    while True:
        if summ == 0: #если это первый проход цикла, считаем единицу, как первую попытку
            summ = summ +1
        number = int(input("загадайте число: \n")) #вводм число
        if number > 50:
            print('Вы ввели недопустимое число, штраф 1 попытка')
            summ +=2
            continue
        full_attemp = attemp - summ  #считаем оставшиеся попытки
        rand = random.randint(1, 50) #задаем промежуток генирации чисел
        if number == rand: #если угадали число выводем его и обнуляем счетчик
            print(f"Вы угадали, это число {rand}")
            summ = 0
            print(f'У Вас сново есть {attemp} попыток')
            sd = input('Хотите сыграть еще? да/нет:\n')
            sd = sd.title()
            if sd == 'Да':
                print('отлично, погнали!')
            else:
                break
        else: #если число не угадали
            if summ == 6: #если счетчк равен 6 обнуляем его
                summ = 0
            if full_attemp == 5 or full_attemp == 0: #сравниваем счетчик для правилького написания
                print(f"число которое Вы ввели {number}, к сожалению оказалось не верным, у Вас осталось {full_attemp} попыток")
            elif full_attemp == 2 or full_attemp == 3 or full_attemp == 4:
                print(f"число которое Вы ввели {number}, к сожалению оказалось не верным, у Вас осталось {full_attemp} попытки")
            elif full_attemp == 1:
                print(f"число которое Вы ввели {number}, к сожалению оказалось не верным, у Вас осталась {full_attemp} попытка")
            if full_attemp == 0:
                s = input('У Вас не осталось попыток, хотте сыграть еще? да/нет:\n')
                s = s.title()
                if s == 'Да':
                    print('отлично, погнали!')
                else:
                    break

            summ = summ+1 #при каждом неправильеом ответе добавляем единицу к счетчику, пока он не достигнет 6
else:
    summ = 0 #задаем счетчик
    attemp = 6 #задаем количество попыток
    print('Game conditions: \n 1) You have 6 attempts to guess the number \n 2) Numbers are guessed from 1 to 50') #условия игры
    while True:
        if summ == 0: #если это первый проход цикла, считаем единицу, как первую попытку
            summ = summ +1
        number = int(input("guess the number: \n")) #вводм число
        if number > 50:
            print('You entered an invalid number, penalty 1 attempt')
            summ +=2
            continue
        full_attemp = attemp - summ  #считаем оставшиеся попытки
        rand = random.randint(1, 50) #задаем промежуток генирации чисел
        if number == rand: #если угадали число выводем его и обнуляем счетчик
            print(f"You guessed it, this number {rand}")
            summ = 0
            print(f'You have {attemp} attempts again')
            sd = input('Want to play some more? yes/no:\n')
            sd = sd.title()
            if sd == 'Yes':
                print('Great, let\'s go!')
            else:
                break
        else: #если число не угадали
            if summ == 6: #если счетчк равен 6 обнуляем его
                summ = 0
            if full_attemp == 5 or full_attemp == 0: #сравниваем счетчик для правилького написания
                print(f"the number you entered {number}, unfortunately turned out to be incorrect, you still have {full_attemp} attempts")
            elif full_attemp == 2 or full_attemp == 3 or full_attemp == 4:
                print(f"the number you entered {number}, unfortunately turned out to be incorrect, you still have {full_attemp} attempts")
            elif full_attemp == 1:
                print(f"the number you entered {number}, unfortunately turned out to be incorrect, you still have {full_attemp} attempt")
            if full_attemp == 0:
                s = input('You have no more attempts, want to play again? yes/no:\n')
                s = s.title()
                if s == 'Yes':
                    print('отлично, погнали!')
                else:
                    break

            summ = summ+1 #при каждом неправильеом ответе добавляем единицу к счетчику, пока он не достигнет 6
