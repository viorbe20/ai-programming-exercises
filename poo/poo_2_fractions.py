"""
Ejercicio 2

Crea una clase, y pruébala, que modele fracciones. Debe permitir:

- Crear fracciones indicando numerador y denominador.
    Ejemplo: f = Fraction(2, 3)
    Ojo!!! No se puede tener un denominador cero.
- Las fracciones pueden operar entre sí.
- Sumar, multiplicar, dividir, restar.
    Ojo!!! esto se puede hacer: f + 1, 5 * f
- Las fracciones se pueden comparar. ==, <, <=, >, >=, !=
    Ojo!!! estas dos fracciones son iguales: 1/2 y 2/4
    Ojo!!! esto se puede hacer 1 < 1/2

Author: Virginia Ordoño Bernier
Date: november 2023
"""
class Fraction:

    def __init__(self, num, den=1):
        # Validación de denominador 0
        self._is_zero_den(den)

        self.__num = num
        self.__den = den

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den

    @num.setter
    def num(self, value):
        if not isinstance(value, int):
            raise ValueError('El numerador debe ser un número entero.')

        self.__num = value

    @den.setter
    def den(self, value):
        if not isinstance(value, int):
            raise ValueError('El denominador debe ser un número entero.')

        self._is_zero_den(value)
        self.__den = value

    def __str__(self):
        return f'{self.__num}/{self.__den}'

    def __repr__(self):
        return f'Fraction({self.__num}, {self.__den})'

    def __add__(self, other):
        if isinstance(other, Fraction):
            lcm = Fraction.get_lcm(self.__den, other.__den)
            num1 = self.__num * (lcm // self.__den)
            num2 = other.__num * (lcm // other.__den)
            return Fraction(num1 + num2, lcm).simplify_fraction()
        else:
            raise ValueError('Dato inválido para la suma.')

    def __sub__(self, other):
        if isinstance(other, Fraction):
            lcm = Fraction.get_lcm(self.__den, other.__den)
            num1 = self.__num * (lcm // self.__den)
            num2 = other.__num * (lcm // other.__den)
            return Fraction(num1 - num2, lcm).simplify_fraction()
        else:
            raise ValueError('Dato inválido para la resta.')

    def __rsub__(self, other):
        if isinstance(other, Fraction):
            lcm = Fraction.get_lcm(self.__den, other.__den)
            num1 = self.__num * (lcm // self.__den)
            num2 = other.__num * (lcm // other.__den)
            return Fraction(num2 - num1, lcm).simplify_fraction()
        else:
            raise ValueError('Dato inválido para la resta.')

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.__num * other.__num, self.__den * other.__den).simplify_fraction()
        elif isinstance(other, int):
            return Fraction(self.__num * other, self.__den).simplify_fraction()
        else:
            raise ValueError('Dato inválido para la multiplicación.')

    def __rmul__(self, other):
        if isinstance(other, int):
            return Fraction(self.__num * other, self.__den).simplify_fraction()
        else:
            raise ValueError('Dato inválido para la multiplicación.')
    def __truediv__(self, other):
            if isinstance(other, Fraction):
                if other.__num == 0:
                    raise ValueError("No se puede dividir por cero.")
                return Fraction(self.__num * other.__den, self.__den * other.__num).simplify_fraction()
            elif isinstance(other, int):
                if other == 0:
                    raise ValueError("No se puede dividir por cero.")
                return Fraction(self.__num, self.__den * other).simplify_fraction()
            else:
                raise ValueError('Dato inválido para la división.')

    def __rtruediv__(self, other):
        if isinstance(other, int):
            if self.__num == 0:
                raise ValueError("No se puede dividir por cero.")
            return Fraction(self.__den * other, self.__num).simplify_fraction()
        else:
            raise ValueError('Dato inválido para la división.')
    def simplify_fraction(self):
        gcd = Fraction.get_gcd(self.__num, self.__den)
        self.__num //= gcd
        self.__den //= gcd
        return self

    @staticmethod
    def _is_zero_den(den):
        if den == 0:
            raise ValueError("El denominador no puede ser 0.")

    @staticmethod
    def get_gcd(den1, den2):
        den1 = abs(den1)
        den2 = abs(den2)

        while den2 > 0:
            rest = den1 % den2
            den1, den2 = den2, rest

        return den1

    @staticmethod
    def get_lcm(den1, den2):
        return abs(den1 * den2) // Fraction.get_gcd(den1, den2)


if __name__ == "__main__":

    # Test 1: create fractions    
    print('\nTest 1: Crear fracciones' )
    print('-'*40)
    print(f'Fraction(6, 3) => {Fraction(6, 3)}')
    

    # Test 2: 0 denominator
    print('\nTest 2: Denominador 0' )
    print('-'*40)
    
    try:
        Fraction(5, 0)
    except ValueError as e:
        print(f'Fraction(5, 0) => Error: {e}')

    # Test 3: fractions operations
    f1 = Fraction(3, 2)
    f2 = Fraction(4, 2)

    print('\nTest 3: Operaciones con fracciones' )
    print('-'*40)
    print(f'{f1} + {f2} = {f1+f2}')
    print(f'{f1} - {f2} = {f1-f2}')
    print(f'{f1} * {f2} = {f1*f2}')
    print(f'{f1} / {f2} = {f1/f2}')
