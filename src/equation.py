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
