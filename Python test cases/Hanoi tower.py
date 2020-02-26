N = int(input())  # Вводим количество дисков


def Hanoi(n, k, m):  # Объявляем фунцию
    if n == 0:
        return
    p = 6 - k - m
    Hanoi(n - 1, k, p)
    print(k, '->', m)  # Выводим пошаговые действия
    Hanoi(n - 1, p, m)


Hanoi(N, 1, 3)
