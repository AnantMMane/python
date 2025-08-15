import sys
from datetime import datetime
from src.models.budget_manager import BudgetManager

def print_menu():
    print("\nPersonal Finance Tracker")
    print("1. Add Transaction")
    print("2. Edit Transaction")
    print("3. Delete Transaction")
    print("4. View Transactions")
    print("5. Add Category")
    print("6. Edit Category")
    print("7. Delete Category")
    print("8. View Categories")
    print("9. View Summary")
    print("10. Exit")

def get_input(prompt: str, required: bool = True) -> str:
    """Get user input with validation."""
    while True:
        value = input(prompt).strip()
        if not required or value:  # Allow empty if not required
            return value
        print("This field is required. Please enter a value.")

def print_summary(summary, title="Summary", alerts=None):
    print(f"\n--- {title} ---")
    print(f"Total Income: ₹{summary['total_income']:.2f}")
    print(f"Total Expenses: ₹{summary['total_expenses']:.2f}")
    print(f"Net Amount: ₹{summary['net_amount']:.2f}")
    print(f"Transaction Count: {summary['transaction_count']}")
    print("\nCategory Breakdown:")
    for cat, vals in summary['category_breakdown'].items():
        print(f"  {cat}: Income ₹{vals.get('income', 0):.2f}, Expense ₹{vals.get('expense', 0):.2f}, Transfer ₹{vals.get('transfer', 0):.2f}")
    if alerts:
        print("\n--- Budget Alerts ---")
        for alert in alerts:
            print(alert)

def view_summary(manager):
    while True:
        print("\nView Summary:")
        print("1. Monthly Summary")
        print("2. Yearly Summary")
        print("3. Last 12 Months Summary (default)")
        print("4. Back to Main Menu")
        choice = get_input("Select an option: ")
        if choice == "1":
            year = get_input("Year (YYYY, leave blank for current): ", required=False)
            month = get_input("Month (1-12, leave blank for current): ", required=False)
            now = datetime.now()
            y = int(year) if year else now.year
            m = int(month) if month else now.month
            summary = manager.get_monthly_summary(y, m)
            alerts = manager.check_budget_alerts(y, m)
            print_summary(summary, title=f"Summary for {y}-{m:02d}", alerts=alerts)
        elif choice == "2":
            year = get_input("Year (YYYY, leave blank for current): ", required=False)
            now = datetime.now()
            y = int(year) if year else now.year
            # Aggregate all months in the year
            from datetime import date
            total_summary = {
                'total_income': 0.0,
                'total_expenses': 0.0,
                'total_transfers': 0.0,
                'net_amount': 0.0,
                'category_breakdown': {},
                'transaction_count': 0
            }
            all_alerts = []
            for m in range(1, 13):
                s = manager.get_monthly_summary(y, m)
                total_summary['total_income'] += s['total_income']
                total_summary['total_expenses'] += s['total_expenses']
                total_summary['total_transfers'] += s['total_transfers']
                total_summary['net_amount'] += s['net_amount']
                total_summary['transaction_count'] += s['transaction_count']
                for cat, vals in s['category_breakdown'].items():
                    if cat not in total_summary['category_breakdown']:
                        total_summary['category_breakdown'][cat] = {'income': 0.0, 'expense': 0.0, 'transfer': 0.0}
                    for k in ['income', 'expense', 'transfer']:
                        total_summary['category_breakdown'][cat][k] += vals.get(k, 0.0)
                all_alerts.extend(manager.check_budget_alerts(y, m))
            print_summary(total_summary, title=f"Yearly Summary for {y}", alerts=all_alerts)
        elif choice == "3":
            # Last 12 months summary
            now = datetime.now()
            from datetime import timedelta
            from collections import defaultdict
            summaries = []
            all_alerts = []
            for i in range(12):
                y = (now.year if now.month - i > 0 else now.year - 1)
                m = (now.month - i - 1) % 12 + 1
                summaries.append(manager.get_monthly_summary(y, m))
                all_alerts.extend(manager.check_budget_alerts(y, m))
            total_summary = {
                'total_income': 0.0,
                'total_expenses': 0.0,
                'total_transfers': 0.0,
                'net_amount': 0.0,
                'category_breakdown': {},
                'transaction_count': 0
            }
            for s in summaries:
                total_summary['total_income'] += s['total_income']
                total_summary['total_expenses'] += s['total_expenses']
                total_summary['total_transfers'] += s['total_transfers']
                total_summary['net_amount'] += s['net_amount']
                total_summary['transaction_count'] += s['transaction_count']
                for cat, vals in s['category_breakdown'].items():
                    if cat not in total_summary['category_breakdown']:
                        total_summary['category_breakdown'][cat] = {'income': 0.0, 'expense': 0.0, 'transfer': 0.0}
                    for k in ['income', 'expense', 'transfer']:
                        total_summary['category_breakdown'][cat][k] += vals.get(k, 0.0)
            print_summary(total_summary, title="Summary for Last 12 Months", alerts=all_alerts)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")

def main():
    manager = BudgetManager()
    while True:
        print_menu()
        choice = get_input("Select an option: ")
        if choice == "1":
            # Add Transaction
            try:
                amount_str = get_input("Amount: ")
                if not amount_str:
                    print("Amount is required.")
                    continue
                
                try:
                    amount = float(amount_str)
                    if amount <= 0:
                        print("Amount must be positive.")
                        continue
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
                    continue
                
                ttype = get_input("Type (income/expense/transfer): ").lower()
                if ttype not in ["income", "expense", "transfer"]:
                    print("Invalid transaction type. Must be 'income', 'expense', or 'transfer'.")
                    continue
                
                category = get_input(f"Category {manager.get_category_names()}: ")
                if not category:
                    print("Category is required.")
                    continue
                
                description = get_input("Description (optional): ", required=False)
                date_str = get_input("Date (YYYY-MM-DD, leave blank for today): ", required=False)
                
                try:
                    date = datetime.strptime(date_str, "%Y-%m-%d") if date_str else None
                except ValueError:
                    print("Invalid date format. Use YYYY-MM-DD.")
                    continue
                
                transaction = manager.add_transaction(amount, ttype, category, description, date)
                print(f"Added: {transaction}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            # Edit Transaction
            tid = get_input("Transaction ID: ")
            transaction = manager.get_transaction_by_id(tid)
            if not transaction:
                print("Transaction not found.")
                continue
            try:
                amount = get_input(f"Amount [{transaction.amount}]: ", required=False)
                ttype = get_input(f"Type [{transaction.type}]: ", required=False)
                category = get_input(f"Category [{transaction.category}]: ", required=False)
                description = get_input(f"Description [{transaction.description}]: ", required=False)
                date_str = get_input(f"Date [{transaction.date.strftime('%Y-%m-%d')}]: ", required=False)
                manager.edit_transaction(
                    tid,
                    amount=float(amount) if amount else None,
                    type=ttype if ttype else None,
                    category=category if category else None,
                    description=description if description else None,
                    date=datetime.strptime(date_str, "%Y-%m-%d") if date_str else None
                )
                print("Transaction updated.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "3":
            # Delete Transaction
            tid = get_input("Transaction ID: ")
            if manager.delete_transaction(tid):
                print("Transaction deleted.")
            else:
                print("Transaction not found.")
        elif choice == "4":
            # View Transactions
            txns = manager.get_transactions()
            if not txns:
                print("No transactions found.")
            else:
                for t in txns:
                    print(f"{t.id}: {t}")
        elif choice == "5":
            # Add Category
            try:
                name = get_input("Category name: ")
                if not name:
                    print("Category name is required.")
                    continue
                
                budget_str = get_input("Budget limit (optional): ", required=False)
                budget = None
                if budget_str:
                    try:
                        budget = float(budget_str)
                        if budget < 0:
                            print("Budget limit cannot be negative.")
                            continue
                    except ValueError:
                        print("Invalid budget limit. Please enter a valid number.")
                        continue
                
                category = manager.add_category(name, budget)
                print(f"Added: {category}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "6":
            # Edit Category
            name = get_input("Category name: ")
            if not name:
                print("Category name is required.")
                continue
                
            if name not in manager.categories:
                print("Category not found.")
                continue
                
            new_name = get_input(f"New name [{name}]: ", required=False)
            budget_str = get_input("Budget limit (optional): ", required=False)
            
            try:
                budget = None
                if budget_str:
                    try:
                        budget = float(budget_str)
                        if budget < 0:
                            print("Budget limit cannot be negative.")
                            continue
                    except ValueError:
                        print("Invalid budget limit. Please enter a valid number.")
                        continue
                
                manager.edit_category(
                    name,
                    new_name=new_name if new_name else None,
                    budget_limit=budget
                )
                print("Category updated.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "7":
            # Delete Category
            name = get_input("Category name: ")
            try:
                if manager.delete_category(name):
                    print("Category deleted.")
                else:
                    print("Category not found or cannot be deleted.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "8":
            # View Categories
            cats = manager.get_categories()
            if not cats:
                print("No categories found.")
            else:
                for c in cats:
                    print(f"{c.name}: {c}")
        elif choice == "9":
            # View Summary
            view_summary(manager)
        elif choice == "10":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main() 