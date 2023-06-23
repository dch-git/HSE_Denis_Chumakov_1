"""
    1. Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и строки и сохраните в переменные, а затем выведите на экран. Используйте функции для консольного ввода input() и консольного вывода print().
Попробуйте также в ходе выполнения задания через встроенную функцию id() понаблюдать, какие типы объектов могут изменяться и сохранять за собой адрес в оперативной памяти.
"""


def show_variables():
    var_bool = bool(input("Please type 'True' or 'False': "))
    print("ID: ", id(var_bool))
    var_string = str(input("Please type any words: "))
    print("ID: ", id(var_string))
    var_int = int(input("Please type any digit: "))
    print("ID: ", id(var_int))
    print("Variables: "
          "Int variable: ", str(var_int), ", ",
          "String variable: ", var_string, ", ",
          "Boolean variable: ", str(var_bool))

show_variables()