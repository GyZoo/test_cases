""" Напишите код, который посчитает сумму всех чисел от 1 до 999, которые
делятся на 3 либо на 5."""

A = []
sum = 0
for i in range(0, 999):
    A.append(i + 1)
    if A[i] % 3 == 0 or A[i] % 5 == 0:
        sum += A[i]
print(sum)