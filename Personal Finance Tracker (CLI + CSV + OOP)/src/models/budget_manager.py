import csv
import os
from datetime import datetime, date
from typing import List, Dict, Optional, Tuple, Union, Literal
from collections import defaultdict

from .transaction import Transaction
from .category import Category
from src.utils import csv_handler


class BudgetManager:
    """
    Main manager class for handling all budget operations.
    
    Manages transactions, categories, and provides summary functionality.
    """
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.transactions: List[Transaction] = []
        self.categories: Dict[str, Category] = {}
        
        # Ensure data directory exists
        os.makedirs(data_dir, exist_ok=True)
        
        # Initialize with predefined categories
        self._initialize_categories()
        
        # Load existing data
        self.load_data()
    
    def _initialize_categories(self) -> None:
        """Initialize with predefined categories."""
        predefined_categories = Category.get_predefined_categories()
        for category in predefined_categories:
            self.categories[category.name] = category
    
    def add_transaction(
        self,
        amount: float,
        type: Union[str, Literal["income", "expense", "transfer"]],
        category: str,
        description: str = "",
        date: Optional[datetime] = None
    ) -> Transaction:
        """Add a new transaction."""
        # Validate amount
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        # Validate category
        if not category or not category.strip():
            raise ValueError("Category must be specified")
        
        category = category.strip()  # Normalize category name
        
        # Validate category exists
        if category not in self.categories:
            raise ValueError(f"Category '{category}' does not exist. Please create it first.")
        
        # Validate transaction type
        if type not in ["income", "expense", "transfer"]:
            raise ValueError("Transaction type must be 'income', 'expense', or 'transfer'")
        
        # Create and add transaction
        transaction = Transaction(amount, type, category, description, date)  # type: ignore
        self.transactions.append(transaction)
        
        # Save to CSV
        self.save_transactions()
        
        return transaction
    
    def edit_transaction(
        self,
        transaction_id: str,
        amount: Optional[float] = None,
        type: Optional[Union[str, Literal["income", "expense", "transfer"]]] = None,
        category: Optional[str] = None,
        description: Optional[str] = None,
        date: Optional[datetime] = None
    ) -> bool:
        """Edit an existing transaction."""
        transaction = self.get_transaction_by_id(transaction_id)
        if not transaction:
            return False
        
        if amount is not None:
            if amount <= 0:
                raise ValueError("Amount must be positive")
            transaction.amount = amount
        if type is not None:
            if type not in ["income", "expense", "transfer"]:
                raise ValueError("Transaction type must be 'income', 'expense', or 'transfer'")
            transaction.type = type
        if category is not None:
            # Validate category
            if not category or not category.strip():
                raise ValueError("Category must be specified")
            
            category = category.strip()  # Normalize category name
            
            if category not in self.categories:
                raise ValueError(f"Category '{category}' does not exist")
            transaction.category = category
        if description is not None:
            transaction.description = description
        if date is not None:
            transaction.date = date
        
        # Save to CSV
        self.save_transactions()
        return True
    
    def delete_transaction(self, transaction_id: str) -> bool:
        """Delete a transaction by ID."""
        transaction = self.get_transaction_by_id(transaction_id)
        if transaction:
            self.transactions.remove(transaction)
            self.save_transactions()
            return True
        return False
    
    def get_transaction_by_id(self, transaction_id: str) -> Optional[Transaction]:
        """Get transaction by ID."""
        for transaction in self.transactions:
            if transaction.id == transaction_id:
                return transaction
        return None
    
    def get_transactions(
        self,
        type_filter: Optional[str] = None,
        category_filter: Optional[str] = None,
        date_from: Optional[date] = None,
        date_to: Optional[date] = None
    ) -> List[Transaction]:
        """Get filtered transactions."""
        filtered_transactions = self.transactions
        
        if type_filter:
            filtered_transactions = [t for t in filtered_transactions if t.type == type_filter]
        
        if category_filter:
            filtered_transactions = [t for t in filtered_transactions if t.category == category_filter]
        
        if date_from:
            filtered_transactions = [t for t in filtered_transactions if t.date.date() >= date_from]
        
        if date_to:
            filtered_transactions = [t for t in filtered_transactions if t.date.date() <= date_to]
        
        # Sort by date (newest first)
        filtered_transactions.sort(key=lambda x: x.date, reverse=True)
        
        return filtered_transactions
    
    def add_category(self, name: str, budget_limit: Optional[float] = None) -> Category:
        """Add a new user-defined category."""
        # Validate category name
        if not name or not name.strip():
            raise ValueError("Category name must be non-empty")
        
        name = name.strip()  # Normalize the name
        
        if name in self.categories:
            raise ValueError(f"Category '{name}' already exists")
        
        # Validate budget limit if provided
        if budget_limit is not None:
            if budget_limit < 0:
                raise ValueError("Budget limit cannot be negative")
        
        category = Category(name, budget_limit, is_predefined=False)
        self.categories[name] = category
        
        # Save categories to CSV
        self.save_categories()
        
        return category
    
    def edit_category(self, name: str, new_name: Optional[str] = None, budget_limit: Optional[float] = None) -> bool:
        """Edit an existing category."""
        if name not in self.categories:
            return False
        
        category = self.categories[name]
        
        # Validate new name if provided (even if it's empty)
        if new_name is not None:
            if not new_name or not new_name.strip():
                raise ValueError("Category name must be non-empty")
            
            new_name = new_name.strip()  # Normalize the name
            
            # Update name if it's different
            if new_name != name:
                if new_name in self.categories:
                    raise ValueError(f"Category '{new_name}' already exists")
                
                # Update category name in transactions
                for transaction in self.transactions:
                    if transaction.category == name:
                        transaction.category = new_name
                
                # Remove old category and add new one
                del self.categories[name]
                category.name = new_name
                self.categories[new_name] = category
        
        # Update budget limit if provided
        if budget_limit is not None:
            if budget_limit < 0:
                raise ValueError("Budget limit cannot be negative")
            category.set_budget_limit(budget_limit)
        
        # Save data
        self.save_categories()
        self.save_transactions()
        
        return True
    
    def delete_category(self, name: str) -> bool:
        """Delete a category (only user-defined categories)."""
        if name not in self.categories:
            return False
        
        category = self.categories[name]
        if category.is_predefined:
            raise ValueError("Cannot delete predefined categories")
        
        # Check if category is used in transactions
        if any(t.category == name for t in self.transactions):
            raise ValueError(f"Cannot delete category '{name}' as it is used in transactions")
        
        del self.categories[name]
        self.save_categories()
        return True
    
    def get_categories(self) -> List[Category]:
        """Get all categories."""
        return list(self.categories.values())
    
    def get_category_names(self) -> List[str]:
        """Get all category names."""
        return list(self.categories.keys())
    
    def get_summary(self, start_date: Optional[date] = None, end_date: Optional[date] = None) -> Dict:
        """Get financial summary for a date range."""
        filtered_transactions = self.get_transactions(date_from=start_date, date_to=end_date)
        
        total_income = sum(t.amount for t in filtered_transactions if t.is_income())
        total_expenses = sum(t.amount for t in filtered_transactions if t.is_expense())
        total_transfers = sum(t.amount for t in filtered_transactions if t.is_transfer())
        
        # Category breakdown
        category_breakdown = defaultdict(lambda: {'income': 0.0, 'expense': 0.0, 'transfer': 0.0})
        for transaction in filtered_transactions:
            category_breakdown[transaction.category][transaction.type] += transaction.amount
        
        return {
            'total_income': total_income,
            'total_expenses': total_expenses,
            'total_transfers': total_transfers,
            'net_amount': total_income - total_expenses,
            'category_breakdown': dict(category_breakdown),
            'transaction_count': len(filtered_transactions)
        }
    
    def get_monthly_summary(self, year: int, month: int) -> Dict:
        """Get summary for a specific month."""
        start_date = date(year, month, 1)
        if month == 12:
            end_date = date(year + 1, 1, 1) - date.resolution
        else:
            end_date = date(year, month + 1, 1) - date.resolution
        
        return self.get_summary(start_date, end_date)
    
    def check_budget_alerts(self, year: int, month: int) -> List[str]:
        """Check for budget limit violations."""
        alerts = []
        monthly_summary = self.get_monthly_summary(year, month)
        
        for category_name, amounts in monthly_summary['category_breakdown'].items():
            category = self.categories.get(category_name)
            if category and category.has_budget_limit():
                total_expense = amounts.get('expense', 0)
                if total_expense > category.budget_limit:
                    overspent = total_expense - category.budget_limit
                    alerts.append(
                        f"Budget Alert: {category_name} exceeded by ₹{overspent:.2f} "
                        f"(Spent: ₹{total_expense:.2f}, Budget: ₹{category.budget_limit:.2f})"
                    )
        
        return alerts
    
    def save_transactions(self) -> None:
        """Save transactions to encrypted CSV file using csv_handler."""
        filepath = os.path.join(self.data_dir, "transactions.csv.enc")
        csv_handler.write_transactions(filepath, self.transactions)

    def save_categories(self) -> None:
        """Save categories to CSV file using csv_handler."""
        filepath = os.path.join(self.data_dir, "categories.csv")
        csv_handler.write_categories(filepath, list(self.categories.values()))

    def load_data(self) -> None:
        """Load data from CSV files."""
        self.load_transactions()
        self.load_categories()
    
    def load_transactions(self) -> None:
        """Load transactions from encrypted CSV file using csv_handler."""
        # Try encrypted file first, fall back to unencrypted for migration
        encrypted_filepath = os.path.join(self.data_dir, "transactions.csv.enc")
        unencrypted_filepath = os.path.join(self.data_dir, "transactions.csv")
        
        if os.path.exists(encrypted_filepath):
            self.transactions = csv_handler.read_transactions(encrypted_filepath)
        elif os.path.exists(unencrypted_filepath):
            # Migrate unencrypted file to encrypted
            self.transactions = csv_handler.read_transactions(unencrypted_filepath)
            # Save as encrypted and remove unencrypted file
            self.save_transactions()
            os.remove(unencrypted_filepath)
        else:
            self.transactions = []

    def load_categories(self) -> None:
        """Load categories from CSV file."""
        try:
            categories = csv_handler.read_categories(os.path.join(self.data_dir, "categories.csv"))
            for category in categories:
                self.categories[category.name] = category
        except FileNotFoundError:
            pass  # File doesn't exist yet, use predefined categories
    
    def search_transactions(self, query: str) -> List[Transaction]:
        """Search transactions by description, category, or amount."""
        query = query.lower().strip()
        if not query:
            return self.transactions
        
        results = []
        for transaction in self.transactions:
            # Search in description
            if query in transaction.description.lower():
                results.append(transaction)
                continue
            
            # Search in category
            if query in transaction.category.lower():
                results.append(transaction)
                continue
            
            # Search in amount (exact match)
            if query == str(int(transaction.amount)):
                results.append(transaction)
                continue
            
            # Search in amount (partial match)
            if query in str(transaction.amount):
                results.append(transaction)
                continue
        
        return results
    
    def get_expense_trends(self, months: int = 6) -> Dict:
        """Get expense trends over the last N months."""
        trends = {}
        current_date = datetime.now()
        year = current_date.year
        month = current_date.month
        for _ in range(months):
            # Always keep month in 1..12 and decrement year accordingly
            if month < 1:
                month = 12
                year -= 1
            summary = self.get_monthly_summary(year, month)
            trends[f"{year}-{month:02d}"] = {
                'total_expenses': summary['total_expenses'],
                'total_income': summary['total_income'],
                'net_amount': summary['net_amount'],
                'transaction_count': summary['transaction_count']
            }
            month -= 1
        return trends
    
    def get_category_performance(self, year: int, month: int) -> Dict:
        """Get performance analysis for each category based on actual income."""
        summary = self.get_monthly_summary(year, month)
        category_data = summary['category_breakdown']
        total_income = summary['total_income']
        
        performance = {}
        for category_name, data in category_data.items():
            category = self.categories.get(category_name)
            if category:
                expense = data.get('expense', 0)
                
                # Calculate budget based on income percentage if category has a budget limit
                if category.budget_limit and total_income > 0:
                    # Use the category's budget limit as a percentage of income
                    budget_limit = category.budget_limit
                    utilization = (expense / budget_limit) * 100 if budget_limit > 0 else 0
                    
                    performance[category_name] = {
                        'expense': expense,
                        'budget_limit': budget_limit,
                        'utilization_percent': utilization,
                        'remaining': budget_limit - expense,
                        'status': 'over_budget' if expense > budget_limit else 'under_budget',
                        'income_percentage': (budget_limit / total_income) * 100 if total_income > 0 else 0
                    }
                elif total_income > 0:
                    # For categories without budget limits, show as percentage of total income
                    income_percentage = (expense / total_income) * 100
                    
                    performance[category_name] = {
                        'expense': expense,
                        'budget_limit': None,
                        'utilization_percent': income_percentage,
                        'remaining': None,
                        'status': 'no_budget_set',
                        'income_percentage': income_percentage
                    }
        
        return performance
    
    def export_data(self, format: str = "csv", filepath: Optional[str] = None) -> str:
        """Export data in various formats."""
        if format.lower() == "csv":
            return self._export_to_csv(filepath)
        elif format.lower() == "json":
            return self._export_to_json(filepath)
        else:
            raise ValueError("Unsupported export format. Use 'csv' or 'json'")
    
    def _export_to_csv(self, filepath: Optional[str] = None) -> str:
        """Export data to CSV format."""
        if not filepath:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = os.path.join(self.data_dir, f"export_{timestamp}.csv")
        
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Date', 'Type', 'Category', 'Amount', 'Description'])
            
            for transaction in self.transactions:
                writer.writerow([
                    transaction.id,
                    transaction.date.strftime('%Y-%m-%d'),
                    transaction.type,
                    transaction.category,
                    transaction.amount,
                    transaction.description
                ])
        
        return filepath
    
    def _export_to_json(self, filepath: Optional[str] = None) -> str:
        """Export data to JSON format."""
        import json
        
        if not filepath:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = os.path.join(self.data_dir, f"export_{timestamp}.json")
        
        export_data = {
            'transactions': [t.to_dict() for t in self.transactions],
            'categories': [c.to_dict() for c in self.categories.values()],
            'export_date': datetime.now().isoformat(),
            'total_transactions': len(self.transactions),
            'total_categories': len(self.categories)
        }
        
        with open(filepath, 'w', encoding='utf-8') as jsonfile:
            json.dump(export_data, jsonfile, indent=2, ensure_ascii=False)
        
        return filepath
    
    def get_financial_insights(self) -> Dict:
        """Get financial insights and recommendations."""
        current_date = datetime.now()
        summary = self.get_monthly_summary(current_date.year, current_date.month)
        performance = self.get_category_performance(current_date.year, current_date.month)
        
        insights = {
            'monthly_summary': summary,
            'category_performance': performance,
            'recommendations': [],
            'alerts': self.check_budget_alerts(current_date.year, current_date.month)
        }
        
        # Generate recommendations
        if summary['total_expenses'] > summary['total_income']:
            insights['recommendations'].append("Your expenses exceed your income this month. Consider reducing spending.")
        
        over_budget_categories = [cat for cat, data in performance.items() if data['status'] == 'over_budget']
        if over_budget_categories:
            insights['recommendations'].append(f"Categories over budget: {', '.join(over_budget_categories)}")
        
        if summary['transaction_count'] == 0:
            insights['recommendations'].append("No transactions recorded this month. Start tracking your finances!")
        
        return insights 
    
    def import_data(self, filepath: str, format: str = "auto") -> Dict:
        """Import data from various formats."""
        if format == "auto":
            if filepath.lower().endswith('.csv'):
                format = "csv"
            elif filepath.lower().endswith('.json'):
                format = "json"
            else:
                raise ValueError("Unsupported file format. Please specify format explicitly.")
        
        if format.lower() == "csv":
            return self._import_from_csv(filepath)
        elif format.lower() == "json":
            return self._import_from_json(filepath)
        else:
            raise ValueError("Unsupported import format. Use 'csv' or 'json'")
    
    def _import_from_csv(self, filepath: str) -> Dict:
        """Import data from CSV format."""
        import csv
        
        imported_count = 0
        errors = []
        
        try:
            with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                
                for row_num, row in enumerate(reader, start=2):  # Start from 2 to account for header
                    try:
                        # Parse transaction data
                        amount = float(row.get('Amount', 0))
                        transaction_type = row.get('Type', '').lower()
                        category = row.get('Category', '').strip()
                        description = row.get('Description', '').strip()
                        date_str = row.get('Date', '')
                        
                        # Validate required fields
                        if not category:
                            errors.append(f"Row {row_num}: Missing category")
                            continue
                        
                        if transaction_type not in ['income', 'expense', 'transfer']:
                            errors.append(f"Row {row_num}: Invalid transaction type '{transaction_type}'")
                            continue
                        
                        # Parse date
                        try:
                            if date_str:
                                date = datetime.strptime(date_str, '%Y-%m-%d')
                            else:
                                date = datetime.now()
                        except ValueError:
                            errors.append(f"Row {row_num}: Invalid date format '{date_str}'")
                            continue
                        
                        # Create transaction
                        transaction = Transaction(amount, transaction_type, category, description, date)  # type: ignore
                        self.transactions.append(transaction)
                        imported_count += 1
                        
                    except (ValueError, KeyError) as e:
                        errors.append(f"Row {row_num}: {str(e)}")
                        continue
            
            # Save imported data
            if imported_count > 0:
                self.save_transactions()
            
            return {
                'imported_count': imported_count,
                'errors': errors,
                'success': len(errors) == 0
            }
            
        except FileNotFoundError:
            raise ValueError(f"File not found: {filepath}")
        except Exception as e:
            raise ValueError(f"Error reading file: {str(e)}")
    
    def _import_from_json(self, filepath: str) -> Dict:
        """Import data from JSON format."""
        import json
        
        try:
            with open(filepath, 'r', encoding='utf-8') as jsonfile:
                data = json.load(jsonfile)
            
            imported_transactions = 0
            imported_categories = 0
            errors = []
            
            # Import categories if present
            if 'categories' in data:
                for cat_data in data['categories']:
                    try:
                        category = Category.from_dict(cat_data)
                        if category.name not in self.categories:
                            self.categories[category.name] = category
                            imported_categories += 1
                    except Exception as e:
                        errors.append(f"Category import error: {str(e)}")
            
            # Import transactions if present
            if 'transactions' in data:
                for txn_data in data['transactions']:
                    try:
                        transaction = Transaction.from_dict(txn_data)
                        self.transactions.append(transaction)
                        imported_transactions += 1
                    except Exception as e:
                        errors.append(f"Transaction import error: {str(e)}")
            
            # Save imported data
            if imported_transactions > 0:
                self.save_transactions()
            if imported_categories > 0:
                self.save_categories()
            
            return {
                'imported_transactions': imported_transactions,
                'imported_categories': imported_categories,
                'errors': errors,
                'success': len(errors) == 0
            }
            
        except FileNotFoundError:
            raise ValueError(f"File not found: {filepath}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error reading file: {str(e)}") 