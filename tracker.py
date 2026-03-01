import json

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def show_expenses(expenses):
    if not expenses:
        print("Расходов пока нет.")
        return
    print("\nСохранённые расходы:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Категория: {expense['category']}, Сумма: {expense['amount']}")

def add_expense(expenses):
    category = input("Введите категорию (еда, такси, игры): ")
    amount = float(input("Введите сумму: "))
    expense = {
        "category": category,
        "amount": amount
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Расход добавлен.")
    return expenses

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def show_stat(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f"Общая сумма расходов: {total}")

def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker")
        print("1. Показать все расходы")
        print("2. Добавить расход")
        print("3. Статистика")
        print("4. Выйти")

        choice = input("Введите команду: ")
        if choice == "1":
            show_expenses(expenses)
        elif choice == "2":
            expenses = add_expense(expenses)
        elif choice == "3" or choice == "stat":
            show_stat(expenses)
        elif choice == "4":
            print("Выход.")
            break
        else:
            print("Неизвестная команда")
main()
