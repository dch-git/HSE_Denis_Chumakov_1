"""
1. Запросите у пользователя через консоль число n (от 1 до 9).
2. Найдите сумму чисел n + nn + nnn.
3. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
4. Выведете данные в консоль.
"""

a = input("Enter a number from 1 to 9: ")

if a.isdigit() and 0 < int(a) < 10:
    b = int(a) + int(a+a) + int(a+a+a)
    print(b)
else:
    print("Error! Wrong value entered. Please enter a number between 1 and 9.")