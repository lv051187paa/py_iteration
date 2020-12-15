"""Sinus calculation module"""
import math


def sin_(angle: float) -> float:
    """returns sinus"""
    result_prescision: int = 9
    counter: int = 0
    result: float = 0
    for iterator in range(result_prescision):
        if iterator == 1:
            result = angle
        if iterator > 1 and iterator % 2 == 1:
            if not counter % 2:
                result -= (angle**3/math.factorial(iterator))
            else:
                result += (angle ** 3 / math.factorial(iterator))
            counter += 1

    return (round(result * 10)) / 10
