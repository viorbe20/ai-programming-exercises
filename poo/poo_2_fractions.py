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
from typeguard import typechecked

@typechecked
class Fraction:

    def __init__(self, num: int, den: int = 1):
        self._is_zero_den(den)
        self.num = num
        self.den = den
    
    @property
    def num(self):
        return self.__num
    
    @property
    def den(self):
        return self.__den
    
    @num.setter
    def num(self, new_value: int):
        self.__num = new_value
            
    @den.setter
    def den(self, new_value: int):
        self._is_zero_den(new_value)
        self.__den = new_value
    
    @staticmethod
    def _is_zero_den(den):
        if den == 0:
            raise ValueError("El denominador no puede ser 0.")
    
    def __str__(self) -> str:
        return f'{self.__num}/{self.__den}'
    
    def __repr__(self):
        # Formal string representation of a Fraction object
        return f'Fraction({self.__num}, {self.__den})'
    
    # Fractions operations
    def simplify_fraction(self):
        gcd = Fraction.get_gcd(self.__num, self.__den)
        self.__num //= gcd
        self.__den //= gcd
        return self
    
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
        #print(abs(den1 * den2) // Fraction.get_gcd(den1, den2))
        return abs(den1 * den2) // Fraction.get_gcd(den1, den2)

    # Comparison operations        
    
    def __lt__(self, other) -> bool:
    # Only int or Fraction
        if isinstance(other, int):
            other = Fraction(other, 1)
        elif not isinstance(other, Fraction):
            raise TypeError('Operador invalido para "<".')
        return (self.__num / self.__den) < (other.num / other.den)

    def __gt__(self, other) -> bool:
    # Only int or Fraction
        if isinstance(other, int):
            other = Fraction(other, 1)
        elif not isinstance(other, Fraction):
            raise TypeError('Operador invalido para ">".')
        return (self.__num / self.__den) > (other.num / other.den)
    
    def __eq__(self, other) -> bool:
        # Only int or Fraction
        if isinstance(other, int):
            other = Fraction(other, 1)
        elif not isinstance(other, Fraction):
            raise TypeError('Operador invalido para "==".')
        return (self.__num / self.__den) == (other.num / other.den)
    
    # Arithmetic operations
    
    def __add__(self, other):
        # Other == int or fractions
        if isinstance(other, int):
            other = Fraction(other, 1)
        elif not isinstance(other, Fraction):
            raise TypeError("Sólo se pueden sumar fracciones o enteros.")

        # Get the least common multiple (LCM) of the denominators
        lcm = Fraction.get_lcm(self.den, other.den)

        # Calculate the new numerators for the summed fractions
        new_num1 = self.num * (lcm // self.den)
        new_num2 = other.num * (lcm // other.den)

        # Calculate the new numerator by adding the obtained numerators
        result_num = new_num1 + new_num2

        # Create and return the new resulting fraction
        return Fraction(result_num, lcm)
    
    def __radd__(self, other:int): 
        return self + other
    
    def __sub__(self, other):
        # Other == int or fractions
        if isinstance(other, int):
            other = Fraction(other, 1)
        elif not isinstance(other, Fraction):
            raise TypeError("Sólo se pueden restar fracciones o enteros.")
        
        # Get the least common multiple (LCM) of the denominators
        lcm = Fraction.get_lcm(self.den, other.den)

        # Calculate the new numerators for the subtracted fractions
        new_num1 = self.num * (lcm // self.den)
        new_num2 = other.num * (lcm // other.den)

        # Calculate the new numerator by subtracting the obtained numerators
        result_num = new_num1 - new_num2

        # Create and return the new resulting fraction
        return Fraction(result_num, lcm)

    def __rsub__(self, other:int):
        return Fraction(other, 1) - other

    def __mul__(self, other):
        # Other == int or fractions
        if isinstance(other, int):
            other = Fraction(other, 1)
        elif not isinstance(other, Fraction):
            raise TypeError("Sólo se pueden multiplicar fracciones o enteros.")
        return Fraction(self.num * other.num, self.den * other.den)
    
    def __rmul__(self, other:int): 
        return self * other

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
    f1 = Fraction(3, 8)
    f2 = Fraction(4, 4)
    num = 5 

    print('\nTest 3: Operaciones con fracciones' )
    print('-'*40)
    print('\nSuma' )
    print('-'*40)
    print(f'{f1} + {f2} = {f1 + f2}')
    print(f'{f2} + {f1} = {f2 + f1}')
    print(f'{f1} + {num} = {f1 + num}')
    print(f'{num} + {f1} = {num + f1}')
    print('\nResta' )
    print('-'*40)
    print(f'{f1} - {f2} = {f1 - f2}')
    print(f'{f2} - {f1} = {f2 - f1}')
    print(f'{f1} - {num} = {f1 - num}')
    print(f'{num} - {f1} = {num - f1}')
    print('\nMultiplicación' )
    print('-'*40)
    print(f'{f1} * {f2} = {f1 * f2}')
    print(f'{f2} * {f1} = {f2 * f1}')
    print(f'{f1} * {num} = {f1 * num}')
    print(f'{num} * {f1} = {num * f1}')

    
    # Ejemplos de comparación
    f3 = Fraction(10, 2)
    num1 = 5

    print('\nTest 4: Comparaciones con fracciones')
    print('-'*40)
    print(f'{f3} < {f3} => {f3 < f3}')
    print(f'{f3} > {f3} => {f3 > f3}')
    print(f'{f3} == {f3} => {f3 == f3}')
    print(f'{f3} < {num1} => {f3 < num1}')
    print(f'{f3} > {num1} => {f3 > num1}')
    print(f'{f3} == {num1} => {f3 == num1}')