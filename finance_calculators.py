#This program is designed for a small financial company
#It allows the user to access two different financial calculators,
#The two calculators are investment and home loan repayment calculator.

import math

print("Welcome to Finance Calculator! To begin:\n")

calc_type = input("""Choose either 'investment' or 'bond' from the menu below to proceed:

investment      - to calculate the amount of interest you will earn on interest
bond            - to calculate the amount you will have to pay on home loan

""")

if ((calc_type == "Investment") or (calc_type == "INVESTMENT") or (calc_type == "investment")):                 #'or' operator used to allow for different capitalisation of text
        amount =float(input("Please enter the amount you are depositing: R"))
        interest_rate = int(input("Please enter interest rate as a percentage: "))
        period = int(input("Please enter the number of years you are investing for: "))
        interest = input("Please select the type of interest you want (simple or compound): ")

        if interest == "simple":                                                                                #branch for the two "interest" options
            total_amount = round(amount * (1 + interest_rate/100 * period),2)
            print("\nThe total amount of an investment with simple interest applied will be: R", total_amount)
        else:                                                                                                   #second "interest option"
            total_amount = round(amount * math.pow((1 + interest_rate/100), period),2)
            print("\nThe total amount of an investment with compound interest applied is: R", total_amount)

elif ((calc_type == "Bond") or (calc_type == "bond") or (calc_type == "BOND")):                                 #second calculator option branch
        house_value = float(input("Please enter the present value of the house: R"))
        interest_rate = int(input("Please enter the rate of interest as a percentage: "))
        period = int(input("Please enter the number of months you plan to take to repay bond: "))
        month_interest = (interest_rate/100)/12                                                                 #converting annual interest rate to monthly interest rate
        
        repayment = round((house_value * month_interest)/(1 - math.pow((1 + month_interest), -period)),2)       #Bond repayment formula
        print("\nThe monthly repayment amount on the bond will be: R", repayment)
else:
    print("\nYou have entered an invalid input! The options are Bond or Investment.")
