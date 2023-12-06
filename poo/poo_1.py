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


class Duration:

    def __init__(self, hours=0, minutes=0, seconds=0):

        # Data type validation
        self._validate_type(hours, "Horas")
        self._validate_type(minutes, "Minutos")
        self._validate_type(seconds, "Segundos")

        # Data adaptation
        minutes += seconds // 60
        seconds %= 60
        hours += minutes // 60
        minutes %= 60

        # Inmutable = no setters
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    @staticmethod
    def _validate_type(value, name):
        if not isinstance(value, int):
            raise TypeError(f"{name} debe ser un número entero")

    def __str__(self):
        return f"{self.__hours}h:{self.__minutes}m:{self.__seconds}s"

    def __eq__(self, other):
        return (self.__hours, self.__minutes, self.__seconds) == (other.hours, other.minutes, other.seconds)

    def __add__(self, other):
        total_seconds = (self.__hours + other.hours) * 3600 + \
            (self.__minutes + other.minutes) * 60 + self.__seconds + other.seconds
        return Duration(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)

    def __sub__(self, other):
        total_seconds = (self.__hours - other.hours) * 3600 + \
            (self.__minutes - other.minutes) * 60 + self.__seconds - other.seconds
        return Duration(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)

    def __rsub__(self, other):
        total_seconds = (other.hours - self.__hours) * 3600 + \
            (other.minutes - self.__minutes) * 60 + other.seconds - self.__seconds
        return Duration(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)


if __name__ == "__main__":

    # Test 1. Transformation

    t1 = Duration()
    t2 = Duration(10, 62, 15)
    t3 = Duration(34)
    t4 = Duration(34, 15)
    t5 = Duration(34, 61)

    print("\nTest 1. Duraciones")
    print("-------------")
    print(f"Duration() = {t1}")
    print(f"Duration(10,62,15) = {t2}")
    print(f"Duration(34) = {t3}")
    print(f"Duration(34, 15) = {t4}")
    print(f"Duration(34, 61) = {t5}")

    # Test 2. Comparison

    t6 = Duration(10, 20, 10)
    t7 = Duration(10, 20, 11)
    t8 = Duration(10, 19, 70)

    print("\nTest 2. Comparar")
    print(f"Duration(10,20,10) == Duration(10,20,10) => {t6 == t6}")
    print(f"Duration(10,20,10) == Duration(10,20,11) => {t6 == t7}")
    print(f"Duration(10,20,10) == Duration(10,19,70) => {t6 == t8}")

    # Test 3. Addition

    print("\nTest 3. Sumar")
    print(f"Duration(10,19,70) + Duration(10,20,10) => {t8 + t6}")

    # Test 4. Subtraction

    t9 = Duration(100, 40, 40)
    t10 = Duration(10, 0, 0)

    print("\nTest 4. Restar")
    print(f"Duration(100,40,40) - Duration(10,0,0) => {t9 - t10}")
    print(f"Duration(10,0,0) - Duration(100,40,40) => {t10 - t9}")

    # Test 5. Add and substract seconds to a duration

    print("\nTest 5. Sumar y restar segundos")
    print(f"Duration(10,0,0) + 10 => {t10 + Duration(seconds=10)}")
    print(f"Duration(10,0,0) - 10 => {t10 - Duration(seconds=10)}")
