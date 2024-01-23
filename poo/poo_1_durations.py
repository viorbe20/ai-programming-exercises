"""
Ejercicio 1

En Python existen clases para manipular duraciones de tiempo (horas:minutos:segundos), 
pero no nos gustan, vamos a hacer una nueva que se llamará Duration y será inmutable. Debe permitir:

- Crear duraciones de tiempos.
    - Ejemplo: t = Duration(10,20,56)
    - Ojo!!! (10, 62, 15) se debe guardar como (11, 2, 15)
    - Si no indico la hora, minuto o segundo estos valores son cero:
        Duration() --> (0, 0, 0)
        Duration(34) --> (34, 0, 0)
        Duration(34, 15) --> (34, 15, 0)
        Duration(34, 61) --> (35, 1, 0)
- Las duraciones de tiempo se pueden comparar.
- A las duraciones de tiempo les puedo sumar y restar segundos.
- Las duraciones de tiempo se pueden sumar y restar. 

Author: Virginia Ordoño Bernier
Date: november 2023
"""
from typing import Type
from typeguard import typechecked

@typechecked
class Duration:

    def __init__(self, hours:int=0, minutes:int = 0, seconds:int=0):

        # Private attributes (name mangling) 
        total__seconds = hours * 3600 + minutes * 60 + seconds
        self.__hours, accumulate = divmod(total__seconds, 3600)
        self.__minutes, self.__seconds = divmod(accumulate, 60)
    
    def _get_total_seconds(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds
    
    def __str__(self):
        return f"{self.__hours:02d}h:{self.__minutes:02d}m:{self.__seconds:02d}s"

    def __lt__(self, other: Type['Duration']): # controlling type of 'other'
        return self._get_total_seconds() < other._get_total_seconds()

    def __eq__(self, other: Type['Duration']): # controlling type of 'other'
        return self._get_total_seconds() == other._get_total_seconds()

    def __gt__(self, other: Type['Duration']): # controlling type of 'other'
        return self._get_total_seconds() > other._get_total_seconds()
    
    def compare(self, other: Type['Duration']):
        if self._get_total_seconds() < other._get_total_seconds():
            return f"{self} es menor que {other}"
        elif  self._get_total_seconds() > other._get_total_seconds():
            return f"{self} es mayor que {other}"
        else:
            return f"{self} es igual que {other}"

    def __add__(self, other):
        if isinstance(other, int):
            total_seconds = self.__hours * 3600 + self.__minutes * 60 + self.__seconds + other
        elif isinstance(other, Duration):
            total_seconds = (
                self.__hours + other.__hours) * 3600 + \
                (self.__minutes + other.__minutes) * 60 + \
                self.__seconds + other.__seconds
        else:
            raise TypeError("Valor no válido")

        return Duration(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, int):
            total_seconds = self.__hours * 3600 + self.__minutes * 60 + self.__seconds - other
        elif isinstance(other, Duration):
            total_seconds = (
                self.__hours - other.__hours) * 3600 + \
                (self.__minutes - other.__minutes) * 60 + \
                self.__seconds - other.__seconds
        else:
            raise TypeError("Valor no válido")

        return Duration(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)

    def __rsub__(self, other: int): # Only for a substraction like: int - Duration. Int 
        return Duration(0, 0, other) - self

if __name__ == "__main__":

    # Test 1. Transformation

    t1 = Duration()
    t2 = Duration(10, 62, 15)
    t3 = Duration(34)
    t4 = Duration(34, 15)
    t5 = Duration(34, 61)

    print("\nTest 1. Duraciones")
    print('-'*40)
    print(f"Duration(10, 62, 15) = {t2}")
    print(f"Duration() = {t1}")
    print(f"Duration(34) = {t3}")
    print(f"Duration(34, 15) = {t4}")
    print(f"Duration(34, 61) = {t5}")

    # Test 2. Comparison

    t6 = Duration(10, 20, 60)
    t7 = Duration(10, 20, 10)

    print('\nTest 2: Comparaciones')
    print('-'*40)
    print(f"Duration(10, 20, 60) == Duration(10, 20, 10) => {t6 == t7}")
    # print(f"Duration(10, 20, 60) == Duration(10, 20, 10) => {t6.compare(t7)}")
    # print(f"Duration(10, 20, 10) == Duration(10, 20, 60) => {t7.compare(t6)}")
    # print(f"Duration(10, 20, 60) == Duration(10, 20, 60) => {t6.compare(t6)}")
    
    # Test 3. Addition and substraction seconds
    
    t6_plus_10 = t6 + 10
    t6_minus_10 = t6 - 70
    t6_rsub_10 = 10 - t6
    
    print('\nTest 3: Sumar y restar segundos')
    print('-'*40)
    print(f"Duration(10, 20, 60) + 10 => {t6_plus_10}")
    print(f"Duration(10, 20, 60) - 10 => {t6_minus_10}")
    print(f"10 - Duration(10, 20, 60) => {t6_rsub_10}")
    
    # Test 4. Addition and substraction of durations
    
    t6_plus_t7 = t6 + t7
    t6_minus_t7 = t6 - t7
    t7_minus_t6 = t7 - t6
    
    print('\nTest 4: Sumar y restar duraciones')
    print('-'*40)
    print(f"Duration(10, 20, 60) + Duration(10, 20, 10) => {t6_plus_t7}")
    print(f"Duration(10, 20, 10) - Duration(10, 20, 60) => {t6_minus_t7}")
    print(f"Duration(10, 20, 60) - Duration(10, 20, 10) => {t7_minus_t6}")