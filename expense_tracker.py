from expense import Expense
import calendar
import datetime


def main():
    print("Running Expense Tracker")
    expense_file_path = "expense.csv"
    budget = 5000

    # Get user input for Expense
    expense = get_user_expense()

    # Write thier expense to a file
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize Expenses.
    summarize_expenses(expense_file_path, budget)


def get_user_expense():
    print("Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    expense_categories = [
        "Food", "Home", "Work", "Fun", "Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}") 

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if i in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount = expense_amount
            )
            return new_expense
        else:
            print("Invalid Category. Please try again.")
            

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving User Expenses: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")
    

def summarize_expenses(expense_file_path, budget):
    print("Summarizing User Expenses.")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            
            line_expense = Expense(
                name = expense_name, amount = float(expense_amount), category = expense_category
            )
            expenses.append(line_expense)
    
    # Sum of amount by Category
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses by Category : ")
    for key, amount in amount_by_category.items():
        print(f"  {key} : Rs.{amount:.2f}")


    # Total spent within a Month
    total_spent = sum([x.amount for x in expenses])
    print(f"You've spent Rs.{total_spent:.2f} this month!")


    # Finding remaining budget for this month
    remaining_amount = budget - total_spent
    print(f"Remaining Budget Rs.{remaining_amount:.2f} for this month!")

    # Getting remaining days of month and Calculate how much I can spent per day
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    print(f"Remaning days in the current month : ", remaining_days)

    daily_budget = remaining_amount / remaining_days
    print(f"Budget Per Day : Rs. {daily_budget:.2f}")



if __name__ == "__main__":
    main()