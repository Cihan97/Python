import datetime 

def days_remanining(deadline):
    today = datetime.datetime.today()
    remaining = (deadline - today).days
    return remaining
# Project delivery deadline
deadline = datetime.datetime(2025, 4, 15) #Project delivery deadline 

# remaning days 
remaining_days = days_remanining(deadline)  


if remaining_days > 0:
    print(f"Project delivery is in {remaining_days} days")
elif remaining_days == 0:
    print("Project delivery is today")
else:
    print("Project delivery is passed! Overdue: {-remaining_days} days")