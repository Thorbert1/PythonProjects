def add(a: float = 0, b: float = 0):
    return a + b


def subtract(a: float = 0, b: float = 0):
    return a - b


def divide(a: float = 0, b: float = 0):
    return a / b


def multiply(a: float = 0, b: float = 0):
    return a * b


def power(basis: float = 0, exponent: int = 0):
    if exponent == 0:
        return 1
    else:
        result = basis
        for _ in range(exponent - 1):
            result *= basis
        return result


def sqrt(radicand: float = 0):
    error = 0.000001
    guess = radicand
    while True:
        result = (1 / 2) * (guess + radicand / guess)
        if abs(result - guess) < error:
            return result
        else:
            guess = result


if __name__ == "__main__":
    sqrt(90)
