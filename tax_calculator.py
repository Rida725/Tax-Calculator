# Tax Calculator Project

def taxable_income(income):
    if income < 0:
        raise ValueError("Income cannot be negative")
    return income


def tax(income):
    income = taxable_income(income)

    amount = 0

    if income > 1000000:
        amount += (income - 1000000) * 0.15
        income = 1000000

    if income > 500000:
        amount += (income - 500000) * 0.10
        income = 500000

    if income > 250000:
        amount += (income - 250000) * 0.05

    return amount


def net_income(income):
    income = taxable_income(income)
    return income - tax(income)


# Main Program

if __name__ == "__main__":

    print("WELCOME TO TAX CALCULATOR")

    annual_income = float(
        input("Enter your annual income: ")
    )

    print("\n----- TAX DETAILS -----")

    print(
        "Taxable Income:",
        taxable_income(annual_income)
    )

    print(
        "Estimated Tax:",
        round(tax(annual_income), 2)
    )

    print(
        "Net Income:",
        round(net_income(annual_income), 2)
    )

    def tax_summary(income):

    income = taxable_income(income)

    return (
        f"Income: Rs. {income:.2f}\n"
        f"Tax: Rs. {tax(income):.2f}\n"
        f"Net Income: Rs. {net_income(income):.2f}"
    )

