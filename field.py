# field trip exercises
# Brayden Towner
# 11/07/2023

def good_morning():
    """
    Prints Good Morning!
    no args
    no return
    """
    print("Good Morning!")

def issue_pay(hours_worked, hourly_pay=32.50):
    """Returns the amount owed to the employee. Remember, you "lost" 2 hours due to them "not clocking in correctly"

    Args:
        hours_worked (int): amount of hours worked
        hourly_pay (float, optional): hourly rate of pay. Defaults to 32.50.
    """
    return hours_worked * hourly_pay

def print_students(*students_names):
    """Prints students names to mimic personal connection so they spend more and are less likely to criticize
        students_names (strings, multiple): Students Names
    """
    for profit_giver in students_names:
        print(profit_giver)

good_morning()


print(f"You owe them {issue_pay(int(input('How many hours have they worked? >  ')))}")

print_students("James", "Brayden", "Micah", "Cameron")
print_students("James", "Brayden", "Micah", "Cameron", "Brayden (different one)", "Allen", "Agent 47", "Stabby McStab face (legal name)")