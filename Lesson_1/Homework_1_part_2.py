"""
1. Пользователь вводит время в секундах. Рассчитайте время и сохраните отдельно в каждую переменную количество часов, минут и секунд.
2. Переведите время в часы, минуты, секунды и сохраните в отдельных переменных.
3. Используйте приведение типов для перевода строк в числовые типы.
4. Предусмотрите проверку строки на наличие только числовых данных через встроенный строковый метод .isdigit()
5. Выведите рассчитанные часы, минуты и секунды по отдельности в консоль.
"""

a = input("Please enter Please enter time in numbers: ")

if a.isdigit():
    seconds = int(a)
    minutes = seconds / 60
    hours = minutes / 60
    print(seconds,"seconds")
    print(seconds, "seconds is", minutes, "minutes")
    print(seconds, "seconds", hours,"hours")
else:
    print("Error! The entered value is incorrect. Please enter the time in DIGITS")