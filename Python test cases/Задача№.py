'''Напишите код, который посчитает количество чисел от 100 до 999, в
которых каждая цифра числа отличается от других цифр не менее, чем на 3
(например: 147, 159, 629, 408 и т.п.). Укажите используемый язык и
прикрепите код полноценного проекта.'''
A = []
List = []
for i in range(100, 1000):
    A.append(i)
    for j in range(len(A)):
        units = A[j] % 10  # Единицы
        decades = A[j] % 100 // 10  # Десятки
        hundreds = A[j] // 100  # Сотни
    if abs(hundreds - decades) >= 3 and abs(hundreds - units) >= 3 and abs(decades - units) >= 3:
        List.append(A[i])
print(List)
