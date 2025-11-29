"""Giai phuong trinh"""


def complexe(a, b, c):
    """Giai phuong trinh"""
    assert (a, b, c) != (0, 0, 0)
    if a != 0:
        delta = b**2 - 4 * a * c
        s = delta**0.5
        return {(-b - s) / (2 / a), (-b + s) / (2 * a)}

    if b != 0:
        return {-c / b}

    return set()



def sans_cube(n):
    """
    Test if n is not divisible by any number of type p³ where p >= 2 is an integer.
    """
    p = 2
    while n != 1:
        if n % p == 0:
            if n % (p**3) == 0:
                return False
            n = n // p
            if n % p == 0:
                n = n // p
        p = p + 1
    return True
