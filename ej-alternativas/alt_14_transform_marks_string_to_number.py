"""
Diseña un programa que, dado un número real que debe representar la calificación numérica de un examen, 
proporcione la calificación cualitativa correspondiente al número dado. 
La calificación cualitativa será una de las siguientes: «Suspenso» (nota menor que 5), 
«Aprobado» (nota mayor o igual que 5, pero menor que 7), «Notable» (nota mayor o igual que 7, pero menor que 9), 
«Sobresaliente» (nota mayor o igual que 9, pero menor que 10), «Matrícula de Honor» (nota 10).
Date: october 2023.
Author: Virginia Ordoño Bernier
"""

print("\nA continuación, dada una calificación numérica, el programa proporcionará la calificación cualitativa correspondiente.\n")


try:
    numerical_grade = float(input("Introduce la nota: "))
except ValueError:
    print("\nValor incorrecto. Inténtalo de nuevo.\n")
    exit()

# Determine the grade

if numerical_grade < 5:
    grade = "Suspenso"
elif numerical_grade >= 5 and numerical_grade < 7:
    grade = "Aprobado"
elif numerical_grade >= 7 and numerical_grade <= 9:
    grade = "Notable"
elif numerical_grade == 10:
    grade = "Matrícula de Honor"
else:
    print("\nValor incorrecto. Inténtalo de nuevo.\n")
    exit()

print(f"\nLa calificación cualitativa es: {grade}.\n")