"""
        2) Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
        Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
        качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
        ошибкой.
        3) Создайте собственный класс-исключение, который должен проверять содержимое списка на
        наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
        запрашивать у пользователя данные и заполнять список только числами. Класс-исключение
        должен контролировать типы данных элементов списка.
        Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
        пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом
        скрипт завершается, сформированный список с числами выводится на экран.
        Подсказка: для данного задания примем, что пользователь может вводить только числа и
        строки. При вводе пользователем очередного элемента необходимо реализовать проверку
        типа элемента и вносить его в список, только если введено число. Класс-исключение должен
        не позволить пользователю ввести текст (не число) и отобразить соответствующее
        сообщение. При этом работа скрипта не должна завершаться.
"""


class OwnZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


print("Попробуем разделить 2 на 0")
a = 2
b = 0
if b == 0:
    raise OwnZeroDivisionError('Попытка деления на ноль.')
else:
    print(a/b)