from typing import Union


def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp == 0:
        return 1
    elif exp == 1:
        return x
    elif exp < 0:
        raise ValueError('This function works only with exp > 0.')
    return x * to_power(x, exp - 1)


assert to_power(2, 3) == 8
assert to_power(3.5, 2) == 12.25
assert to_power(2, -1)
