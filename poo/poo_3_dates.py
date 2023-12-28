"""
En Python podemos manejar fechas pero no nos gustan. Vamos a crear una clase Date que puede permitir:

1. Crear fechas
Ejemplos:
f = Date(17, 11, 2022)
Fechas erróneas:
- Negativos. Date(78, -45, 0)
- Días fuera del mes. Date(31, 6, 2022)
- Día 29 de febrero en no bisiesto. Date(29, 2, 2022)

2. Las fechas se pueden comparar

3. A las fechas se les pueden sumar y restar días

4. Se debe poder averiguar el día de la semana de una fecha

autora: Virginia Ordoño Bernier 
"""

class Date:
    MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    DAYS_IN_WEEK = 7

    def __init__(self, day, month, year):
        self._validate_date(day, month, year)
        self.__day = day
        self.__month = month
        self.__year = year

    @staticmethod
    def _validate_date(day, month, year):
        # Verificar que el mes esté en el rango permitido
        if not (1 <= month <= 12):
            raise ValueError("Mes debe estar entre 1 y 12")

        # Verificar que el año sea mayor a cero
        if year <= 0:
            raise ValueError("Año debe ser mayor a cero")

        # Verificar que el día sea mayor a cero
        if day <= 0:
            raise ValueError("Día debe ser mayor a cero")

        # Verificar que el día esté dentro del rango permitido
        if not (1 <= day <= Date.MONTH_DAYS[month] or (month == 2 and day == 29 and Date.is_leap_year(year))):
            if month == 2 and day == 29:
                raise ValueError(f"El 29 de febrero solo es válido en años bisiestos. {year} no es bisiesto")
            else:
                raise ValueError("Día fuera de rango para el mes dado")


    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def __str__(self):
        return f"{self.__day:02d}/{self.__month:02d}/{self.__year}"

    def __lt__(self, other):
        return (self.__year, self.__month, self.__day) < (other.__year, other.__month, other.__day)

    def __le__(self, other):
        return (self < other) or (self == other)

    def __gt__(self, other):
        return (self.__year, self.__month, self.__day) > (other.__year, other.__month, other.__day)

    def __ge__(self, other):
        return (self > other) or (self == other)
    
    def compare(self, other):
        if self < other:
            return f"{self} es anterior a {other}"
        elif self > other:
            return f"{self} es posterior a {other}"
        else:
            return f"{self} es igual a {other}"

    def day_of_week(self):
        days_since_start = self._get_days_amount_since_start()
        days_offset = 4  # 1/1/1970 was a Thursday (4th day of the week)

        # Get number day and then name day
        day_number = (days_since_start + days_offset) % Date.DAYS_IN_WEEK
        day_names = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        day_name = day_names[day_number]

        return day_name

    def _get_days_amount_since_start(self):
        days = 0
        for year in range(1970, self.__year):
            days += 366 if Date.is_leap_year(year) else 365
        for month in range(1, self.__month):
            days += Date.MONTH_DAYS[month]
            if month == 2 and Date.is_leap_year(self.__year):
                days += 1
        days += self.__day - 1
        return days

    def add_days(self, days):
        new_day = self.__day + days
        new_month = self.__month
        new_year = self.__year

        while new_day > Date.MONTH_DAYS[new_month]:
            new_day -= Date.MONTH_DAYS[new_month]
            new_month += 1
            if new_month > 12:
                new_month = 1
                new_year += 1

        return Date(new_day, new_month, new_year)

    def subtract_days(self, days):
        new_day = self.__day - days
        new_month = self.__month
        new_year = self.__year

        while new_day < 1:
            new_month -= 1
            if new_month < 1:
                new_month = 12
                new_year -= 1
            new_day += Date.MONTH_DAYS[new_month]
            if new_month == 2 and Date.is_leap_year(new_year):
                new_day += 1

        return Date(new_day, new_month, new_year)


if __name__ == "__main__":
    
    # Test 1: Creating dates
    
    print('\nTest 1: Creación de fechas')
    print('-'*40)
    print(f'Date(17, 11, 2022) => {Date(17, 11, 2022)}')
    
    # Testing errors
    try:
        Date(31, 6, 2022)  # Error out of range
    except ValueError as e:
        print(f'Date(31, 6, 2022) => Error al crear la fecha: {e}')

    try:
        Date(-31, 6, 2022)  # Error negative day
    except ValueError as e:
        print(f'Date(-31, 6, 2022) => Error al crear la fecha: {e}')

    try:
        Date(29, 2, 2022)  # Error no leap year
    except ValueError as e:
        print(f'Date(29, 2, 2022) => Error al crear la fecha: {e}')

    # Test 2: Comparing dates
    date1 = Date(1, 1, 2022)
    date2 = Date(1, 2, 2022)

    print('\nTest 2: Comparación de fechas')
    print('-'*40)
    print(f"{date1} == {date2} => {date1.compare(date2)}")
    print(f"{date2} == {date1} => {date2.compare(date1)}")
    print(f"{date1} == {date1} => {date1.compare(date1)}")

    # Test 3: Add and substract dates

    print('\nTest 3: Suma y resta de días')
    print('-'*40)
    print(f"{date1} + 31 días => {date1.add_days(31)}")
    print(f"{date1} - 1 día => {date1.subtract_days(1)}")
    
    # Test 4: Guess day of week

    print('\nTest 4: Averigua el día de la semana que es')
    print('-'*40)
    print(f"El {date1} es => {date1.day_of_week()}")