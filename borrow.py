def home():
    print("\n")
    print(" Welcome to the Mortgage Calculator")
    print("\n")
    print(" To find out how much you can potentially borrow please type 'Borrow'.")
    print("\n")
    print(" To find out the repayment amounts please type 'Repayment'.")
    print("\n")
    choice = input("> ")
    if "Borrow" in choice or "borrow" in choice:
        borrow_calc()
    elif "Repayment" in choice or "repayment" in choice:
        repayment_calc()

def borrow_calc():
    print("\n")
    print(" Great, this calculator will tell you how much you can potentially borrow.")
    print("\n")
    print(" Please enter your annual household income?", end=' ')
    income = int(input())
    print("\n")
    print(" Please enter any outgoings you have on a monthly basis?", end=' ')
    outgoings = int(input())
    print("\n")
    outgoings_annual = outgoings * 12
    print(" Finally, please enter your deposit amount?", end=' ')
    deposit = int(input())
    print("\n")
    max_borrow = (income - outgoings_annual)*4
    max_house_price = (max_borrow + deposit)
    print(f" Based on the figures you have provided the maximum property value you can purchase is {max_house_price}.")
    print(f" This is based on your maximum borrowing amount of {max_borrow} plus your deposit amount of {deposit}.")
    print("\n")
    play = input(" Hit enter to go back to the main menu.")
    print("\n")
    home()

def repayment_calc():
    print("\n")
    print(" Great, this calculator will tell you how much your repayments will be.")
    print("\n")
    print(" Please enter the total cost of the property?", end=' ')
    property = float(input())
    print("\n")
    print(" Please enter your deposit amount?", end=' ')
    deposit = float(input())
    print("\n")
    print(" Please enter your mortgage lengh in years?", end=' ')
    lengh = float(input())
    lengh_monthly = float(lengh * 12)

    print("\n")
    print(" Please enter the interest rate? As of April 2022, the best rate on the market is 2.10%", end=' ')
    interest_rate = float(input())
    print("\n")
    interest_monthly = interest_rate / 100 / 12
    loan_amount = property - deposit
    monthly_amount = loan_amount * ((interest_monthly * ((1 + interest_monthly) ** lengh_monthly)) / ((1 + interest_monthly) ** lengh_monthly - 1))
    monthly_amount = int(monthly_amount)
    print(f" Based on the figures you have provided, your payment amount will be £{monthly_amount} per month.")
    print("\n")
    play = input(" Hit enter to go back to the main menu.")
    print("\n")
    home()

home()
