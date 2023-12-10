"""
Hacer un programa que nos permita calcular la cuota de una hipoteca y su tabla de amortización 
después de que se pida al usuario/a:
- Importe del préstamo.
- La tasa de interés anual.
- Y el plazo de pago en años.
Necesitaréis averiguar cómo se hace este cálculo (podéis preguntar a ChatGPT).
Date: october 2023.
Author: Virginia Ordoño Bernier
"""
print("El siguiente programa te pedira unos datos para calcular tu hipoteca y la tabla de amortización.")

loan_amount = float(input("\nIntroduce el importa del préstamo: "))
annual_interest_rate = float(input("\nIntroduce la tada del interés anual: "))
loan_term_years = int(input("\nIntroduce el plazo de pagos (número de años): "))

# Annual interest to monthly interest
monthly_interest_rate = annual_interest_rate / 12 / 100

# Years to month loan term
loan_term_months = loan_term_years * 12

monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -loan_term_months)

print(f"\nPago mensual: {monthly_payment:.2f}")

# Generate and display the amortization table
print("\nAmortization Table:")
print("Month | Initial Balance | Interest Payment | Principal Payment | Total Payment")

balance = loan_amount

# Iterates through each month from 1 to the total number of months in the loan term
for month in range(1, loan_term_months + 1):
    interest_payment = balance * monthly_interest_rate #  Calculates the interest payment for the current month
    principal_payment = monthly_payment - interest_payment # Calculates the principal payment for the current month
    balance -= principal_payment # Updates the remaining loan balance

    print(f"{month}\t\t{balance:.2f}\t\t{interest_payment:.2f}\t\t{principal_payment:.2f}\t\t{monthly_payment:.2f}")
