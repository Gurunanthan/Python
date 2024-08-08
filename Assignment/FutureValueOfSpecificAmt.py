def compute_future_value(principal, rate, years):
    rate = rate / 100
    future_value = principal * (1 + rate) ** years
    return future_value
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
years = int(input("Enter the number of years: "))
future_value = compute_future_value(principal, rate, years)
print(f"The future value of the investment is: ${future_value:.2f}")
