# a budget calculator

def calculate_budget(monthly_income, rent_expense, food_expense, entertainment_expense):
    total_expenses = rent_expense + food_expense + entertainment_expense
    remaining_money = monthly_income - total_expenses
    print("=== BUDGET SUMMARY ===")
    print(f"Monthly Income: ${monthly_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Money: ${remaining_money:.2f}")
    if remaining_money < 0:
        print ("Budget Advice: You're overspending! Cut back on expenses.")
    elif remaining_money < 100:
        print ("Budget Advice: Your budget is tight. Be careful with spending.")
    else:
        print ("Budget Advice: Great job! You have money left over.")


stop = False
while stop == False:
    try:
        monthly_income = float(input("Enter your monthly income: "))
        rent_expense = float(input("Enter rent expense: "))
        food_expense = float(input("Enter food expense: "))
        entertainment_expense = float(input("Enter entertainment expense: "))
        calculate_budget(monthly_income, rent_expense, food_expense, entertainment_expense)
    except ValueError:
        print("Enter a valid price! ")
    except Exception as e:
        print(f"Something went wrong: {e}")
        continue
    stop_variable = input("To stop calculating press: No/N ")
    if stop_variable.lower() in ["no", "n"]:
        stop = True

        