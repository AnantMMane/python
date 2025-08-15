import tkinter as tk
from tkinter import ttk, messagebox
from src.models.budget_manager import BudgetManager
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class FinanceTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Personal Finance Tracker")
        self.geometry("700x500")
        self.manager = BudgetManager()
        self.create_widgets()

    def create_widgets(self):
        # Navigation buttons
        nav_frame = tk.Frame(self)
        nav_frame.pack(side=tk.TOP, fill=tk.X)
        tk.Button(nav_frame, text="Dashboard", command=self.show_dashboard).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(nav_frame, text="Transactions", command=self.show_transactions).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(nav_frame, text="Categories", command=self.show_categories).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(nav_frame, text="Visualizations", command=self.open_visualizations_window).pack(side=tk.LEFT, padx=5, pady=5)
        # Main content area
        self.content = tk.Frame(self)
        self.content.pack(fill=tk.BOTH, expand=True)
        self.show_dashboard()

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_content()
        summary = self.manager.get_monthly_summary(self.manager.transactions[-1].date.year, self.manager.transactions[-1].date.month) if self.manager.transactions else self.manager.get_monthly_summary(2023, 1)
        tk.Label(self.content, text="Dashboard", font=("Arial", 18, "bold")).pack(pady=10)
        tk.Label(self.content, text=f"Total Income: ₹{summary['total_income']:.2f}", fg="green").pack()
        tk.Label(self.content, text=f"Total Expenses: ₹{summary['total_expenses']:.2f}", fg="red").pack()
        tk.Label(self.content, text=f"Net Amount: ₹{summary['net_amount']:.2f}", fg="blue").pack()
        tk.Label(self.content, text=f"Transactions this month: {summary['transaction_count']}").pack(pady=5)
        # Placeholder for recent transactions
        tk.Label(self.content, text="Recent Transactions:", font=("Arial", 12, "bold")).pack(pady=5)
        recent = self.manager.get_transactions()[:5]
        for t in recent:
            tk.Label(self.content, text=str(t)).pack(anchor='w')
        # Budget alerts (bottom right corner)
        from datetime import datetime
        now = datetime.now()
        alerts = self.manager.check_budget_alerts(now.year, now.month)
        if alerts:
            alert_frame = tk.Frame(self.content, bg="#ffcccc", bd=2, relief=tk.RIDGE)
            alert_frame.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)
            tk.Label(alert_frame, text="Budget Alerts!", bg="#ffcccc", fg="red", font=("Arial", 12, "bold")).pack(padx=10, pady=(5,0))
            for alert in alerts:
                tk.Label(alert_frame, text=alert, bg="#ffcccc", fg="red", font=("Arial", 10, "bold"), wraplength=250, justify='left').pack(anchor='w', padx=10, pady=2)
        # Average expense alerts (bottom left corner)
        avg_alerts = self.get_average_expense_alerts(now.year, now.month)
        if avg_alerts:
            avg_alert_frame = tk.Frame(self.content, bg="#fff3cd", bd=2, relief=tk.RIDGE)
            avg_alert_frame.place(relx=0.0, rely=1.0, anchor='sw', x=10, y=-10)
            tk.Label(avg_alert_frame, text="3-Month Avg Alerts!", bg="#fff3cd", fg="#b8860b", font=("Arial", 12, "bold")).pack(padx=10, pady=(5,0))
            for alert in avg_alerts:
                tk.Label(avg_alert_frame, text=alert, bg="#fff3cd", fg="#b8860b", font=("Arial", 10, "bold"), wraplength=250, justify='left').pack(anchor='w', padx=10, pady=2)

    def get_average_expense_alerts(self, year, month):
        # Calculate average expense for each category over the previous 3 months
        from datetime import datetime
        alerts = []
        # Get previous 3 months (handle year wrap)
        months = []
        y, m = year, month
        for _ in range(3):
            m -= 1
            if m == 0:
                m = 12
                y -= 1
            months.append((y, m))
        # Get all categories
        categories = [c.name for c in self.manager.get_categories()]
        for cat in categories:
            # Average over previous 3 months
            prev_expenses = []
            for (y, m) in months:
                s = self.manager.get_monthly_summary(y, m)
                val = s['category_breakdown'].get(cat, {}).get('expense', 0)
                prev_expenses.append(val)
            avg = sum(prev_expenses) / 3 if prev_expenses else 0
            # Current month
            curr = self.manager.get_monthly_summary(year, month)['category_breakdown'].get(cat, {}).get('expense', 0)
            if avg > 0 and curr > avg:
                alerts.append(f"{cat}: Current ₹{curr:.2f} > 3-mo avg ₹{avg:.2f} (+₹{curr-avg:.2f})")
        return alerts

    def show_transactions(self):
        self.clear_content()
        tk.Label(self.content, text="Transactions", font=("Arial", 16, "bold")).pack(pady=10)
        # Table
        columns = ("id", "date", "type", "category", "amount", "description")
        self.txn_tree = ttk.Treeview(self.content, columns=columns, show="headings", height=12)
        for col in columns:
            self.txn_tree.heading(col, text=col.capitalize())
            self.txn_tree.column(col, width=100 if col != "description" else 200)
        self.txn_tree.pack(fill=tk.BOTH, expand=True)
        self.refresh_transactions_table()
        # Buttons
        btn_frame = tk.Frame(self.content)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Add Transaction", command=self.add_transaction_dialog).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Edit Selected", command=self.edit_selected_transaction).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete Selected", command=self.delete_selected_transaction).pack(side=tk.LEFT, padx=5)

    def refresh_transactions_table(self):
        for row in self.txn_tree.get_children():
            self.txn_tree.delete(row)
        for t in self.manager.get_transactions():
            self.txn_tree.insert("", tk.END, values=(t.id, t.date.strftime('%Y-%m-%d'), t.type, t.category, f"₹{t.amount:.2f}", t.description))

    def add_transaction_dialog(self):
        self.transaction_form_dialog("Add Transaction")

    def edit_selected_transaction(self):
        selected = self.txn_tree.selection()
        if not selected:
            messagebox.showwarning("No selection", "Please select a transaction to edit.")
            return
        txn_id = self.txn_tree.item(selected[0])['values'][0]
        txn = self.manager.get_transaction_by_id(txn_id)
        if txn:
            self.transaction_form_dialog("Edit Transaction", txn)

    def delete_selected_transaction(self):
        selected = self.txn_tree.selection()
        if not selected:
            messagebox.showwarning("No selection", "Please select a transaction to delete.")
            return
        txn_id = self.txn_tree.item(selected[0])['values'][0]
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this transaction?"):
            self.manager.delete_transaction(txn_id)
            self.refresh_transactions_table()
            self.show_dashboard()

    def transaction_form_dialog(self, title, txn=None):
        form = tk.Toplevel(self)
        form.title(title)
        form.geometry("350x350")
        # Fields
        tk.Label(form, text="Amount:").pack()
        amount_var = tk.StringVar(value=str(txn.amount) if txn else "")
        tk.Entry(form, textvariable=amount_var).pack()
        tk.Label(form, text="Type (income/expense/transfer):").pack()
        type_var = tk.StringVar(value=txn.type if txn else "expense")
        tk.Entry(form, textvariable=type_var).pack()
        tk.Label(form, text="Category:").pack()
        category_var = tk.StringVar(value=txn.category if txn else "")
        tk.Entry(form, textvariable=category_var).pack()
        tk.Label(form, text="Description:").pack()
        desc_var = tk.StringVar(value=txn.description if txn else "")
        tk.Entry(form, textvariable=desc_var).pack()
        tk.Label(form, text="Date (YYYY-MM-DD):").pack()
        date_var = tk.StringVar(value=txn.date.strftime('%Y-%m-%d') if txn else "")
        tk.Entry(form, textvariable=date_var).pack()
        def on_submit():
            try:
                amount_str = amount_var.get().strip()
                if not amount_str:
                    messagebox.showerror("Error", "Amount is required.")
                    return
                
                try:
                    amount = float(amount_str)
                    if amount <= 0:
                        messagebox.showerror("Error", "Amount must be positive.")
                        return
                except ValueError:
                    messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")
                    return
                
                ttype = type_var.get().lower()
                if ttype not in ["income", "expense", "transfer"]:
                    messagebox.showerror("Error", "Invalid transaction type. Must be 'income', 'expense', or 'transfer'.")
                    return
                
                category = category_var.get().strip()
                if not category:
                    messagebox.showerror("Error", "Category is required.")
                    return
                
                description = desc_var.get().strip()
                date_str = date_var.get().strip()
                
                date = None
                if date_str:
                    try:
                        from datetime import datetime
                        date = datetime.strptime(date_str, "%Y-%m-%d")
                    except ValueError:
                        messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
                        return
                
                if txn:
                    self.manager.edit_transaction(txn.id, amount=amount, type=ttype, category=category, description=description, date=date)
                else:
                    self.manager.add_transaction(amount, ttype, category, description, date)
                self.refresh_transactions_table()
                self.show_dashboard()
                form.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        tk.Button(form, text="Submit", command=on_submit).pack(pady=10)
        tk.Button(form, text="Cancel", command=form.destroy).pack()

    def show_categories(self):
        self.clear_content()
        tk.Label(self.content, text="Categories", font=("Arial", 16, "bold")).pack(pady=10)
        # Table
        columns = ("name", "budget_limit", "is_predefined")
        self.cat_tree = ttk.Treeview(self.content, columns=columns, show="headings", height=10)
        for col in columns:
            self.cat_tree.heading(col, text=col.replace('_', ' ').capitalize())
            self.cat_tree.column(col, width=120)
        self.cat_tree.pack(fill=tk.BOTH, expand=True)
        self.refresh_categories_table()
        # Buttons
        btn_frame = tk.Frame(self.content)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Add Category", command=self.add_category_dialog).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Edit Selected", command=self.edit_selected_category).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete Selected", command=self.delete_selected_category).pack(side=tk.LEFT, padx=5)

    def refresh_categories_table(self):
        for row in self.cat_tree.get_children():
            self.cat_tree.delete(row)
        for c in self.manager.get_categories():
            self.cat_tree.insert("", tk.END, values=(c.name, c.budget_limit if c.budget_limit is not None else '', c.is_predefined))

    def add_category_dialog(self):
        self.category_form_dialog("Add Category")

    def edit_selected_category(self):
        selected = self.cat_tree.selection()
        if not selected:
            messagebox.showwarning("No selection", "Please select a category to edit.")
            return
        name = self.cat_tree.item(selected[0])['values'][0]
        cat = self.manager.categories.get(name)
        if cat:
            self.category_form_dialog("Edit Category", cat)

    def delete_selected_category(self):
        selected = self.cat_tree.selection()
        if not selected:
            messagebox.showwarning("No selection", "Please select a category to delete.")
            return
        name = self.cat_tree.item(selected[0])['values'][0]
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this category?"):
            try:
                self.manager.delete_category(name)
                self.refresh_categories_table()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def category_form_dialog(self, title, cat=None):
        form = tk.Toplevel(self)
        form.title(title)
        form.geometry("300x220")
        # Fields
        tk.Label(form, text="Name:").pack()
        name_var = tk.StringVar(value=cat.name if cat else "")
        tk.Entry(form, textvariable=name_var).pack()
        tk.Label(form, text="Budget Limit (optional):").pack()
        budget_var = tk.StringVar(value=str(cat.budget_limit) if cat and cat.budget_limit is not None else "")
        tk.Entry(form, textvariable=budget_var).pack()
        def on_submit():
            try:
                name = name_var.get().strip()
                if not name:
                    messagebox.showerror("Error", "Category name is required.")
                    return
                
                budget_str = budget_var.get().strip()
                budget = None
                if budget_str:
                    try:
                        budget = float(budget_str)
                        if budget < 0:
                            messagebox.showerror("Error", "Budget limit cannot be negative.")
                            return
                    except ValueError:
                        messagebox.showerror("Error", "Invalid budget limit. Please enter a valid number.")
                        return
                
                if cat:
                    self.manager.edit_category(cat.name, new_name=name, budget_limit=budget)
                else:
                    self.manager.add_category(name, budget)
                self.refresh_categories_table()
                form.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        tk.Button(form, text="Submit", command=on_submit).pack(pady=10)
        tk.Button(form, text="Cancel", command=form.destroy).pack()

    def open_visualizations_window(self):
        from datetime import datetime
        now = datetime.now()
        summary = self.manager.get_monthly_summary(now.year, now.month)
        category_data = summary['category_breakdown']
        # Only show categories with expenses
        labels = []
        sizes = []
        for cat, vals in category_data.items():
            if vals.get('expense', 0) > 0:
                labels.append(cat)
                sizes.append(vals['expense'])
        if not sizes:
            messagebox.showinfo("No Data", "No expenses to visualize for this month.")
            return
        # Create new window
        win = tk.Toplevel(self)
        win.title("Expense Visualizations (Current Month)")
        win.geometry("600x900")
        # Pie chart
        fig1, ax1 = plt.subplots(figsize=(5, 4))
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        ax1.set_title(f"Expense Breakdown by Category\n{now.year}-{now.month:02d}")
        canvas1 = FigureCanvasTkAgg(fig1, master=win)
        canvas1.draw()
        canvas1.get_tk_widget().pack(fill=tk.BOTH, expand=False, pady=(10, 0))
        # Bar chart
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        ax2.bar(labels, sizes, color='skyblue')
        ax2.set_ylabel('Amount (₹)')
        ax2.set_xlabel('Category')
        ax2.set_title(f"Monthly Expenses by Category\n{now.year}-{now.month:02d}")
        ax2.tick_params(axis='x', rotation=30)
        for i, v in enumerate(sizes):
            ax2.text(i, v + max(sizes)*0.01, f"₹{v:.2f}", ha='center', va='bottom', fontsize=9)
        fig2.tight_layout()
        canvas2 = FigureCanvasTkAgg(fig2, master=win)
        canvas2.draw()
        canvas2.get_tk_widget().pack(fill=tk.BOTH, expand=False, pady=(10, 10))

if __name__ == "__main__":
    app = FinanceTrackerApp()
    app.mainloop() 