print("Welcome to XYZ Bank Pvt. Ltd.")
print("1. Withdraw cash. ")
print("2. Renew password. ")
print("3. Deposit cash. ")
print("4. Check existing balance. ")
op = input("What would you like to perform(1/2/3/4) -> ")

if float(op) == 1.0:
    print(" Methods for withdrawing Cash: ")
    print("     1. Fast withdrawal. ")
    print("     2. Enter amount. ")
    meWC = input("      What method would you prefer for cash withdrawal(1/2) -> ")
    if float(meWC) == 1.0:
        print("         Fast withdrawal options: ")
        print("             1. Rs. 1,000.00")
        print("             2. Rs. 2,000.00")
        print("             3. Rs. 5,000.00")
        print("             4. Rs. 10,000.00")
        amWC = float(input("Amount to be withdrawn(1/2/3/4) -> "))
        if amWC == 1.0:
            print("Rs. 1,000.00 have successfully been deducted from your account.")
            print("Initial Balance -> Rs. 1,00,000.00      Current balance -> Rs. 99,000.00")
            print(" Thank you for using XYZ Bank Pvt. Ltd.")
        elif amWC == 2.0:
            print("Rs. 2,000.00 have successfully been deducted from your account.")
            print("Initial Balance -> Rs. 1,00,000.00      Current balance -> Rs. 98,000.00")
            print(" Thank you for using XYZ Bank Pvt. Ltd.")
        elif amWC == 3.0:
            print("Rs. 5,000.00 have successfully been deducted from your account.")
            print("Initial Balance -> Rs. 1,00,000.00      Current balance -> Rs. 95,000.00")
            print(" Thank you for using XYZ Bank Pvt. Ltd.")
        elif amWC == 4.0:
            print("Rs. 10,000.00 have successfully been deducted from your account.")
            print("Initial Balance -> Rs. 1,00,000.00      Current balance -> Rs. 90,000.00")
            print(" Thank you for using XYZ Bank Pvt. Ltd.")
        else:
            print("Oops! Invalid input!")
    elif float(meWC) == 2.0:
        amWC = float(input("  Enter the amount to be withdrawn -> Rs."))
        if amWC > 10000.0:
            print("Invalid Input! Withdrawal can be of a maximum of Rs. 10,000.00 for one transaction.")
        else:
            print(" Rs.", amWC, " have successfully been deducted from your account.")
            rem = float(100000 - amWC)
            print("Initial Balance -> Rs. 1,00,000.00      Current balance -> Rs. ", rem)
            print(" Thank you for using XYZ Bank Pvt. Ltd.")
    else:
        print("Oops! Invalid input!")
elif float(op) == 2.0:
    print(" Password renewal: ")
    Eid = input(" Enter your Email-id for verification -> ")
    print(" Click on the 'VERIFY' button in the email sent to ", Eid, " .")
    pswrd = float(input(" Enter the new password(only numbers) -> "))
    Cpswrd = float(input("Confirm password -> "))
    if pswrd != Cpswrd:
        print(" Do not change password while confirming it. ")
    else:
        print(" Your password has been changed to -> ", pswrd)
        print(" Thank you for using XYZ Bank Pvt. Ltd.")
elif float(op) == 3.0:
    print(" Depositing Cash")
    amDC = float(input(" Enter the amount of cash to be deposited: "))
    print(" Rs.", amDC, " have been deposited into your account successfully.")
    rem = float(100000 + amDC)
    print("Initial Balance -> Rs. 1,00,000.00      Current balance -> Rs. ", rem)
    print(" Thank you for using XYZ Bank Pvt. Ltd.")
elif float(op) == 4.0:
    print(" Checking existing balance in account: ")
    print(" Existing balance in your account is Rs. 1,00,000.00")
    print(" Thank you for using XYZ Bank Pvt. Ltd.")
else:
    print(" Invalid choice input!")
