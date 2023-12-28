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

    def day_of_week(self):
        days_since_epoch = self._calculate_days_since_epoch()
        days_offset = 4  # 1/1/1970 was a Thursday (4th day of the week)
        day_of_week = (days_since_epoch + days_offset) % Date.DAYS_IN_WEEK
        return day_of_week

    def _calculate_days_since_epoch(self):
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
    date3 = Date(1, 1, 2022)
    date4 = Date(1, 2, 2022)


    print('\nTest 2: Comparación de fechas')
    print('-'*40)
    # print(f"{date3} < {date4}: {date3 < date4}")
    # print(f"{date3} <= {date4}: {date3 <= date4}")
    # print(f"{date4} > {date3}: {date4 > date3}")
    # print(f"{date4} >= {date3}: {date4 >= date3}")

    # try:
    #     print(f"{date4} > {date5}: {date4 > date5}")
    # except ValueError as e:
    #     print(f"Error al comparar fechas: {e}")

    # # Test 3: Day of the week
    # date6 = Date(28, 12, 2022)
    # print(f"Día de la semana para {date6}: {date6.day_of_week()}")

    # # Test 4: Adding and subtracting days
    # date7 = Date(1, 1, 2023)
    # date8 = date7.add_days(10)
    # date9 = date7.subtract_days(5)

    # print(f"{date7} + 10 days = {date8}")
    # print(f"{date7} - 5 days = {date9}")
