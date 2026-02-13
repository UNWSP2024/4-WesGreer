# budget program
# written by wesley greer on 2/13/2026

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    ######################
    # Write a program that asks the user to enter the amount that he or she has budgeted for a month.
print("If you tell me your expenses for this month, I can tell you if you're over or under budget.")
print('When you are done entering expenses, simply enter 0 to exit.')
budget = float(input("How much did you budget for this month? $"))
# A loop should then prompt the user to enter each of his or her expenses for the month
more_expense = True
total_expense = 0
while more_expense == True:
    expense = float(input('Enter an expense: $'))
    if expense < 0:
        print('Error: Please enter a valid number.')
        expense = float(input('Enter an expense: $'))
    else: pass
    if expense == 0:
        more_expense = False
    else: pass
    total_expense += expense
# print the amount the user is over or under budget
print(f"The total amount you spent this month is ${total_expense:.2f}")
if total_expense > budget:
    budget_dif = total_expense - budget
    print(f'Oh no! You went ${budget_dif:.2f} over your budget.')
elif total_expense == budget:
    print('Nice! Your expenses were exactly equal to your budget!')
else:
    budget_dif = budget - total_expense
    print(f'Congrats! You stayed ${budget_dif:.2f} under your budget!')
    ######################


if __name__ == '__main__':
    main()
