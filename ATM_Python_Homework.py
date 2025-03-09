# Let's assume the account blance is 1000 unit initially 
account_balance = 1000

# Greet the user and show the current balance 
print("Welcome!")
print("Your current balance is: ", account_balance)

# Let's perform a withdrawal 
withdrawal_amount = float(input("Enter the amount you want to withdraw: "))

# subract the withdrawal amount from the account balance
account_balance = account_balance - withdrawal_amount

# Display the new balance
print("Your new balance is: ", account_balance)

# Let's perform a deposit
deposit_amount = float(input("Enter the amount you want to deposit: "))

# add the deposit amount to the account balance
account_balance = account_balance + deposit_amount

#finally, show the update balance 
print("Your updated balance is: ", account_balance)


