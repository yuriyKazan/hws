def mult(a: int, n: int) -> int:
    if a < 0 or n < 0:
        raise ValueError("This function works only with positive integers")
    if a == 0 or n == 0:
        return 0
    return a + mult(a, n-1)


mult(2, 4) == 8
mult(2, 0) == 0
mult(2, -4)
