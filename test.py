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
        return abs(self.__den)
    
    @num.setter
    def num(self, new_value: int):
        self.__num = new_value
            
    @den.setter
    def den(self, new_value: int):
        self._is_zero_den(new_value)
        self.__den = abs(new_value)
    
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
        return Fraction(other, 1) * self
    
    def __truediv__(self, other):
        # Other == int or fractions
        if isinstance(other, int):
            other = Fraction(other, 1)
        elif not isinstance(other, Fraction):
            raise TypeError("Sólo se pueden dividir fracciones o enteros.")

        # Multiply by the reciprocal (invert the numerator and denominator)
        reciprocal = Fraction(other.den, other.num)

        # Use the reciprocal for division
        return self * reciprocal
    
    def __rtruediv__(self, other:int):
        return Fraction(other, 1) / self


if __name__ == '__main__':
    # Test 3: fractions operations
    f1 = Fraction(3, 8)
    f2 = Fraction(4, 4)
    num = 5 

    print('\nTest 3: Operaciones con fracciones' )
    print('-'*40)
    print(f'{f1} + {f2} = {f1 + f2}')
    print(f'{f2} + {f1} = {f2 + f1}')
    print(f'{f1} + {num} = {f1 + num}')
    print(f'{num} + {f1} = {num + f1}')
    print(f'{f1} - {f2} = {f1 - f2}')
    print(f'{f2} - {f1} = {f2 - f1}')
    print(f'{f1} - {num} = {f1 - num}')
    print(f'{num} - {f1} = {num - f1}')
print(f'{f1} * {f2} = {f1 * f2}')
print(f'{f2} * {f1} = {f2 * f1}')
print(f'{f1} * {num} = {f1 * num}')
print(f'{num} * {f1} = {num * f1}')
print(f'{f1} / {f2} = {f1 / f2}')
print(f'{f2} / {f1} = {f2 / f1}')
print(f'{f1} / {num} = {f1 / num}')
print(f'{num} / {f1} = {num / f1}')
