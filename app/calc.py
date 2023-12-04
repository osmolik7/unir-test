import app
from app import util
import math

class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y

    def raiz_cuadrada(self, x):
        self.check_types(x, 0)
        if x < 0:
            raise ValueError("La raíz cuadrada de un número negativo no es posible")
        return math.sqrt(x)

    def logaritmo_base_10(self, x):
        self.check_types(x, 0)
        if x <= 0:
            raise ValueError("El logaritmo de un número no positivo no es posible")
        return math.log10(x)


    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    resultado = calc.add(2, 2)
    print(resultado)
    resultado = calc.substract(5, 3)
    print(resultado)
    resultado = calc.multiply(4, 6)
    print(resultado)
    resultado = calc.divide(8, 2)
    print(resultado)
    resultado = calc.power(2, 3)
    print(resultado)
    resultado = calc.raiz_cuadrada(9)
    print(resultado)
    resultado = calc.logaritmo_base_10(100)
    print(resultado)
