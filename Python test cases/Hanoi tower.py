N = int(input())


def Hanoi(n, k, m):
    if n == 0:
        return
    p = 6 - k - m
    Hanoi(n - 1, k, p)
    print(k, '->', m)
    Hanoi(n - 1, p, m)


Hanoi(N, 1, 3)
