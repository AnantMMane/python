import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedWidget, QMessageBox, QTableWidget, QTableWidgetItem, QDialog, QFormLayout, QLineEdit, QComboBox, QDateEdit, QFrame, QScrollArea, QFileDialog, QCheckBox
)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QColor
AlignHCenter = getattr(Qt, "AlignHCenter", 0x0004)
AlignCenter = getattr(Qt, "AlignCenter", 0x0004)
AlignRight = getattr(Qt, "AlignRight", 0x0002)
AlignLeft = getattr(Qt, "AlignLeft", 0x0001)
AlignVCenter = getattr(Qt, "AlignVCenter", 0x0080)
def get_alignment():
    # PyQt6
    if hasattr(Qt, 'AlignmentFlag'):
        return Qt.Alignment(Qt.AlignmentFlag.AlignHCenter)
    # PyQt5
    if hasattr(Qt, 'AlignHCenter'):
        return Qt.Alignment(getattr(Qt, 'AlignHCenter'))
    # Fallback (should never be needed, but just in case)
    return Qt.Alignment(Qt.AlignmentFlag(4)) 
from src.models.budget_manager import BudgetManager
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

# Modern styling constants
MODERN_BUTTON_STYLE = """
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #667eea, stop:1 #764ba2);
    border: none;
    border-radius: 10px;
    color: white;
    font-weight: 600;
    padding: 12px 24px;
    font-size: 14px;
    min-height: 24px;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #5a6fd8, stop:1 #6a4190);
}
QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #4a5fc8, stop:1 #5a3180);
}
QPushButton:disabled {
    background: #e0e0e0;
    color: #999999;
}
"""

# Fallback style in case gradients don't work
FALLBACK_BUTTON_STYLE = """
QPushButton {
    background: #667eea;
    border: none;
    border-radius: 10px;
    color: white;
    font-weight: 600;
    padding: 12px 24px;
    font-size: 14px;
    min-height: 24px;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QPushButton:hover {
    background: #5a6fd8;
}
QPushButton:pressed {
    background: #4a5fc8;
}
QPushButton:disabled {
    background: #e0e0e0;
    color: #999999;
}
"""

# Enhanced navigation button style with light blue design
NAV_BUTTON_STYLE = """
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #3b82f6, stop:1 #1d4ed8);
    border: 1px solid #1e40af;
    border-radius: 6px;
    color: white;
    font-weight: 600;
    padding: 12px 20px;
    font-size: 14px;
    margin: 2px;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #2563eb, stop:1 #1e40af);
    border: 1px solid #1d4ed8;
}
QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1e40af, stop:1 #1e3a8a);
    border: 1px solid #1e3a8a;
}
"""

# Fallback navigation button style
FALLBACK_NAV_BUTTON_STYLE = """
QPushButton {
    background: #3b82f6;
    border: 1px solid #1e40af;
    border-radius: 6px;
    color: white;
    font-weight: 600;
    padding: 12px 20px;
    font-size: 14px;
    margin: 2px;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QPushButton:hover {
    background: #2563eb;
    border: 1px solid #1d4ed8;
}
QPushButton:pressed {
    background: #1e40af;
    border: 1px solid #1e3a8a;
}
"""

# Submenu button style
SUBMENU_BUTTON_STYLE = """
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #475569, stop:1 #64748b);
    border: 1px solid #334155;
    border-radius: 4px;
    color: white;
    font-weight: 500;
    padding: 8px 16px;
    font-size: 13px;
    margin: 1px;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #64748b, stop:1 #94a3b8);
    border: 1px solid #475569;
}
QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #334155, stop:1 #475569);
    border: 1px solid #334155;
}
"""

# Fallback submenu button style
FALLBACK_SUBMENU_BUTTON_STYLE = """
QPushButton {
    background: #475569;
    border: 1px solid #334155;
    border-radius: 4px;
    color: white;
    font-weight: 500;
    padding: 8px 16px;
    font-size: 13px;
    margin: 1px;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QPushButton:hover {
    background: #64748b;
    border: 1px solid #475569;
}
QPushButton:pressed {
    background: #334155;
    border: 1px solid #334155;
}
"""

CLEAR_BUTTON_STYLE = """
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ff6b6b, stop:1 #ee5a52);
    border: none;
    border-radius: 8px;
    color: white;
    font-weight: 600;
    padding: 10px 20px;
    font-size: 13px;
    margin: 2px;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ff5252, stop:1 #d32f2f);
}
QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #d32f2f, stop:1 #b71c1c);
}
"""

# Fallback clear button style
FALLBACK_CLEAR_BUTTON_STYLE = """
QPushButton {
    background: #ff6b6b;
    border: none;
    border-radius: 8px;
    color: white;
    font-weight: 600;
    padding: 10px 20px;
    font-size: 13px;
    margin: 2px;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QPushButton:hover {
    background: #ff5252;
}
QPushButton:pressed {
    background: #d32f2f;
}
"""

# Settings button style (same as clear button)
SETTINGS_BUTTON_STYLE = """
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ff6b6b, stop:1 #ee5a52);
    border: none;
    border-radius: 8px;
    color: white;
    font-weight: 600;
    padding: 10px 20px;
    font-size: 13px;
    margin: 2px;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ff5252, stop:1 #d32f2f);
}
QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #d32f2f, stop:1 #b71c1c);
}
"""

# Fallback settings button style
FALLBACK_SETTINGS_BUTTON_STYLE = """
QPushButton {
    background: #ff6b6b;
    border: none;
    border-radius: 8px;
    color: white;
    font-weight: 600;
    padding: 10px 20px;
    font-size: 13px;
    margin: 2px;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QPushButton:hover {
    background: #ff5252;
}
QPushButton:pressed {
    background: #d32f2f;
}
"""

# Enhanced card styles
INCOME_CARD_STYLE = """
QFrame {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #e8f5e8, stop:1 #d4edda);
    border-radius: 16px;
    padding: 24px;
    border: 1px solid #c3e6cb;
}
QFrame:hover {
}
"""

EXPENSE_CARD_STYLE = """
QFrame {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ffeaea, stop:1 #f8d7da);
    border-radius: 16px;
    padding: 24px;
    border: 1px solid #f5c6cb;
}
QFrame:hover {
}
"""

NET_CARD_STYLE = """
QFrame {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #e3f2fd, stop:1 #bbdefb);
    border-radius: 16px;
    padding: 24px;
    border: 1px solid #90caf9;
}
QFrame:hover {
}
"""

# Enhanced table styles
MODERN_TABLE_STYLE = """
QTableWidget {
    background-color: white;
    gridline-color: #e9ecef;
    border: 1px solid #dee2e6;
    border-radius: 12px;
    selection-background-color: #e3f2fd;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 13px;
}
QHeaderView::section {
    background-color: #f8f9fa;
    padding: 14px 10px;
    border: none;
    border-bottom: 2px solid #dee2e6;
    font-weight: 600;
    color: #495057;
    font-size: 13px;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QTableWidget::item {
    padding: 10px;
    border-bottom: 1px solid #f8f9fa;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QTableWidget::item:selected {
    background-color: #e3f2fd;
    color: #000000;
    font-weight: 500;
}
QTableWidget::item:hover {
    background-color: #f8f9fa;
}
"""

# Enhanced form styles
MODERN_FORM_STYLE = """
QLineEdit, QComboBox, QDateEdit {
    padding: 12px;
    border: 2px solid #e9ecef;
    border-radius: 8px;
    background-color: white;
    font-size: 14px;
    min-height: 24px;
    font-family: 'Segoe UI', Arial, sans-serif;
    color: #495057;
}
QLineEdit:focus, QComboBox:focus, QDateEdit:focus {
    border: 2px solid #667eea;
    background-color: #f8f9fa;
    outline: none;
}
QLineEdit:hover, QComboBox:hover, QDateEdit:hover {
    border: 2px solid #adb5bd;
}
QComboBox::drop-down {
    border: none;
    width: 24px;
}
QComboBox::down-arrow {
    image: none;
    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    border-top: 6px solid #6c757d;
    margin-right: 8px;
}
QComboBox QAbstractItemView {
    border: 2px solid #667eea;
    border-radius: 8px;
    background-color: white;
    selection-background-color: #e3f2fd;
    font-family: 'Segoe UI', Arial, sans-serif;
}
"""

class DashboardWidget(QWidget):
    def __init__(self, manager: BudgetManager, parent=None):
        super().__init__(parent)
        self.manager = manager
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        # Set white background
        self.setStyleSheet("background-color: white;")
        # Cache for performance
        self._cached_summary = None
        self._cache_timestamp = None
        self.refresh_dashboard()
    
    def _get_cached_summary(self, force_refresh=False):
        """Get cached summary data with optional force refresh."""
        from datetime import datetime, timedelta
        
        current_time = datetime.now()
        
        # Check if cache is valid (5 minutes)
        if (not force_refresh and 
            self._cached_summary is not None and 
            self._cache_timestamp is not None and
            current_time - self._cache_timestamp < timedelta(minutes=5)):
            return self._cached_summary
        
        # Get fresh data
        current_month = current_time.month
        current_year = current_time.year
        
        if self.manager.transactions:
            summary = self.manager.get_monthly_summary(current_year, current_month)
        else:
            summary = self.manager.get_monthly_summary(2023, 1)
        
        # Update cache
        self._cached_summary = summary
        self._cache_timestamp = current_time
        
        return summary

    def refresh_dashboard(self):
        # Remove all widgets
        while self.main_layout.count():
            child = self.main_layout.takeAt(0)
            if child is not None:
                widget = child.widget()
                if widget is not None:
                    widget.deleteLater()
        # Center content
        center = QVBoxLayout()
        # Title
        title = QLabel("Dashboard")
        title.setStyleSheet("font-size: 32px; font-weight: 700; margin-bottom: 24px; color: #2c3e50; font-family: 'Segoe UI', Arial, sans-serif;")
        center.addWidget(title, alignment=get_alignment())
        # Get current month and year
        from datetime import datetime
        current_month = datetime.now().month
        current_year = datetime.now().year
        
        # Summary cards
        summary = self._get_cached_summary()
        card_layout = QHBoxLayout()
        
        # Modern card styling
        income_card = QFrame()
        income_card.setStyleSheet(INCOME_CARD_STYLE)
        income_label = QLabel(f"Total Income\n₹{summary['total_income']:.2f}")
        income_label.setStyleSheet("font-size: 22px; font-weight: 600; color: #155724; font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.4;")
        income_label.setAlignment(get_alignment())
        income_card_layout = QVBoxLayout()
        income_card_layout.addWidget(income_label)
        income_card.setLayout(income_card_layout)
        
        expense_card = QFrame()
        expense_card.setStyleSheet(EXPENSE_CARD_STYLE)
        expense_label = QLabel(f"Total Expenses\n₹{summary['total_expenses']:.2f}")
        expense_label.setStyleSheet("font-size: 22px; font-weight: 600; color: #721c24; font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.4;")
        expense_label.setAlignment(get_alignment())
        expense_card_layout = QVBoxLayout()
        expense_card_layout.addWidget(expense_label)
        expense_card.setLayout(expense_card_layout)
        
        net_card = QFrame()
        net_card.setStyleSheet(NET_CARD_STYLE)
        net_label = QLabel(f"Net Amount\n₹{summary['net_amount']:.2f}")
        net_label.setStyleSheet("font-size: 22px; font-weight: 600; color: #0d47a1; font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.4;")
        net_label.setAlignment(get_alignment())
        net_card_layout = QVBoxLayout()
        net_card_layout.addWidget(net_label)
        net_card.setLayout(net_card_layout)
        
        card_layout.addWidget(income_card)
        card_layout.addWidget(expense_card)
        card_layout.addWidget(net_card)
        center.addLayout(card_layout)
        # Transactions count
        txn_count = QLabel(f"Transactions this month: <b>{summary['transaction_count']}</b>")
        txn_count.setStyleSheet("font-size: 16px; margin-top: 24px; color: #6c757d; font-family: 'Segoe UI', Arial, sans-serif;")
        center.addWidget(txn_count, alignment=get_alignment())
        
        # Add financial insights
        insights = self.manager.get_financial_insights()
        if insights['recommendations'] or insights['alerts']:
            insights_frame = QFrame()
            insights_frame.setStyleSheet("""
                QFrame {
                    background: #fff3cd;
                    border: 1px solid #ffeaa7;
                    border-radius: 12px;
                    padding: 16px;
                    margin: 16px 0px;
                }
            """)
            insights_layout = QVBoxLayout()
            
            insights_title = QLabel("💡 Financial Insights")
            insights_title.setStyleSheet("font-size: 18px; font-weight: 600; color: #856404; font-family: 'Segoe UI', Arial, sans-serif; margin-bottom: 8px;")
            insights_layout.addWidget(insights_title)
            
            # Add recommendations
            for recommendation in insights['recommendations']:
                rec_label = QLabel(f"• {recommendation}")
                rec_label.setStyleSheet("font-size: 14px; color: #856404; font-family: 'Segoe UI', Arial, sans-serif; margin: 2px 0px;")
                rec_label.setWordWrap(True)
                insights_layout.addWidget(rec_label)
            
            # Add alerts
            for alert in insights['alerts']:
                alert_label = QLabel(f"⚠️ {alert}")
                alert_label.setStyleSheet("font-size: 14px; color: #721c24; font-family: 'Segoe UI', Arial, sans-serif; margin: 2px 0px;")
                alert_label.setWordWrap(True)
                insights_layout.addWidget(alert_label)
            
            insights_frame.setLayout(insights_layout)
            center.addWidget(insights_frame)
        
        # Add budget performance summary
        # Validate month and year before calling get_category_performance
        if 1 <= current_month <= 12 and current_year > 0:
            performance = self.manager.get_category_performance(current_year, current_month)
            if performance:
                performance_frame = QFrame()
                performance_frame.setStyleSheet("""
                    QFrame {
                        background: #f8f9fa;
                        border: 1px solid #dee2e6;
                        border-radius: 12px;
                        padding: 16px;
                        margin: 16px 0px;
                    }
                """)
                perf_layout = QVBoxLayout()
                
                perf_title = QLabel("📊 Budget Performance")
                perf_title.setStyleSheet("font-size: 18px; font-weight: 600; color: #495057; font-family: 'Segoe UI', Arial, sans-serif; margin-bottom: 12px;")
                perf_layout.addWidget(perf_title)
                
                # Show top 3 categories by utilization
                sorted_performance = sorted(performance.items(), key=lambda x: x[1]['utilization_percent'], reverse=True)
                for i, (category_name, data) in enumerate(sorted_performance[:3]):
                    if data['status'] == 'no_budget_set':
                        # Categories without budget limits
                        perf_text = f"📊 {category_name}: {data['income_percentage']:.1f}% of income (₹{data['expense']:.0f})"
                        perf_label = QLabel(perf_text)
                        perf_label.setStyleSheet("font-size: 14px; color: #6c757d; font-family: 'Segoe UI', Arial, sans-serif; margin: 2px 0px;")
                    else:
                        # Categories with budget limits
                        status_icon = "🔴" if data['status'] == 'over_budget' else "🟢"
                        if data['budget_limit']:
                            perf_text = f"{status_icon} {category_name}: {data['utilization_percent']:.1f}% used (₹{data['expense']:.0f}/{data['budget_limit']:.0f})"
                        else:
                            perf_text = f"{status_icon} {category_name}: {data['utilization_percent']:.1f}% of income (₹{data['expense']:.0f})"
                        perf_label = QLabel(perf_text)
                        perf_label.setStyleSheet("font-size: 14px; color: #495057; font-family: 'Segoe UI', Arial, sans-serif; margin: 2px 0px;")
                    
                    perf_layout.addWidget(perf_label)
                
                performance_frame.setLayout(perf_layout)
                center.addWidget(performance_frame)
        
        # Current Month Transactions Table
        
        # Get current month transactions
        current_month_transactions = []
        if self.manager.transactions:
            current_month_transactions = [
                t for t in self.manager.transactions 
                if t.date.month == current_month and t.date.year == current_year
            ]
        
        if current_month_transactions:
            # Table title
            table_title = QLabel(f"Current Month Transactions ({current_month}/{current_year})")
            table_title.setStyleSheet("font-size: 20px; font-weight: 600; margin-top: 32px; margin-bottom: 16px; color: #2c3e50; font-family: 'Segoe UI', Arial, sans-serif;")
            center.addWidget(table_title, alignment=get_alignment())
            
            # Create table
            table = QTableWidget()
            table.setColumnCount(5)
            table.setHorizontalHeaderLabels(["Date", "Type", "Category", "Amount", "Description"])
            table.setRowCount(len(current_month_transactions))
            
            # Style the table
            table.setStyleSheet(MODERN_TABLE_STYLE)
            
            # Populate table
            for row, transaction in enumerate(current_month_transactions):
                # Date
                date_item = QTableWidgetItem(transaction.date.strftime('%Y-%m-%d'))
                date_item.setTextAlignment(AlignCenter)
                table.setItem(row, 0, date_item)
                
                # Type with color coding
                type_item = QTableWidgetItem(transaction.type.capitalize())
                type_item.setTextAlignment(AlignCenter)
                if transaction.type == "income":
                    type_item.setBackground(QColor("#e8f5e8"))
                    type_item.setForeground(QColor("#155724"))
                elif transaction.type == "expense":
                    type_item.setBackground(QColor("#ffeaea"))
                    type_item.setForeground(QColor("#721c24"))
                else:  # transfer
                    type_item.setBackground(QColor("#e3f2fd"))
                    type_item.setForeground(QColor("#0d47a1"))
                table.setItem(row, 1, type_item)
                
                # Category
                category_item = QTableWidgetItem(transaction.category)
                category_item.setTextAlignment(AlignCenter)
                table.setItem(row, 2, category_item)
                
                # Amount with color coding
                amount_text = f"₹{transaction.amount:.2f}"
                amount_item = QTableWidgetItem(amount_text)
                amount_item.setTextAlignment(AlignRight | AlignVCenter)
                if transaction.type == "income":
                    amount_item.setForeground(QColor("#155724"))
                elif transaction.type == "expense":
                    amount_item.setForeground(QColor("#721c24"))
                else:  # transfer
                    amount_item.setForeground(QColor("#0d47a1"))
                table.setItem(row, 3, amount_item)
                
                # Description
                desc_item = QTableWidgetItem(transaction.description or "")
                desc_item.setTextAlignment(AlignLeft | AlignVCenter)
                table.setItem(row, 4, desc_item)
            
            # Set table properties
            table.setAlternatingRowColors(True)
            table.setSelectionBehavior(QTableWidget.SelectRows)
            table.setEditTriggers(QTableWidget.NoEditTriggers)  # Read-only
            table.resizeColumnsToContents()
            
            # Set maximum height for table with scroll
            table.setMaximumHeight(300)
            
            # Add table to layout
            center.addWidget(table)
        else:
            # No transactions message
            no_txn_label = QLabel("No transactions for the current month")
            no_txn_label.setStyleSheet("font-size: 16px; margin-top: 32px; color: #adb5bd; font-style: italic; font-family: 'Segoe UI', Arial, sans-serif;")
            center.addWidget(no_txn_label, alignment=get_alignment())
        
        center.addStretch()
        self.main_layout.addLayout(center)

    def clear_expenses(self):
        reply = QMessageBox.question(self, 'Confirm', 'Are you sure you want to delete all transactions?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.manager.transactions.clear()
            self.manager.save_transactions()
            QMessageBox.information(self, 'Cleared', 'All transactions have been deleted.')
            self.refresh_dashboard()

class TransactionsWidget(QWidget):
    def __init__(self, manager: BudgetManager, parent=None):
        super().__init__(parent)
        self.manager = manager
        # Set white background
        self.setStyleSheet("background-color: white;")
        # Performance optimizations
        self._cached_transactions = None
        self._filtered_transactions = None
        self._current_page = 0
        self._page_size = 50  # Show 50 transactions per page
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        # Add search functionality
        search_layout = QHBoxLayout()
        search_label = QLabel("Search:")
        search_label.setStyleSheet("font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; color: #495057;")
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by description, category, or amount...")
        self.search_input.setStyleSheet(MODERN_FORM_STYLE)
        self.search_input.textChanged.connect(self.filter_transactions)
        
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)
        search_layout.addStretch()
        layout.addLayout(search_layout)
        
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Date", "Type", "Category", "Amount", "Description"])
        self.table.setStyleSheet(MODERN_TABLE_STYLE)
        self.refresh_table()
        layout.addWidget(self.table)
        btn_layout = QHBoxLayout()
        add_btn = QPushButton("Add Transaction")
        edit_btn = QPushButton("Edit Selected")
        del_btn = QPushButton("Delete Selected")
        add_btn.setStyleSheet(FALLBACK_BUTTON_STYLE)
        edit_btn.setStyleSheet(FALLBACK_BUTTON_STYLE)
        del_btn.setStyleSheet(FALLBACK_BUTTON_STYLE)
        add_btn.clicked.connect(self.add_transaction)
        edit_btn.clicked.connect(self.edit_transaction)
        del_btn.clicked.connect(self.delete_transaction)
        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(edit_btn)
        btn_layout.addWidget(del_btn)
        layout.addLayout(btn_layout)
        self.setLayout(layout)
    
    def filter_transactions(self):
        """Filter transactions based on search query."""
        query = self.search_input.text().strip()
        if not query:
            self.refresh_table()
            return
        
        # Get filtered transactions
        filtered_transactions = self.manager.search_transactions(query)
        
        # Update table with filtered results
        self.table.setRowCount(len(filtered_transactions))
        for row, t in enumerate(filtered_transactions):
            self.table.setItem(row, 0, QTableWidgetItem(t.id))
            self.table.setItem(row, 1, QTableWidgetItem(t.date.strftime('%Y-%m-%d')))
            self.table.setItem(row, 2, QTableWidgetItem(t.type))
            self.table.setItem(row, 3, QTableWidgetItem(t.category))
            self.table.setItem(row, 4, QTableWidgetItem(f"₹{t.amount:.2f}"))
            self.table.setItem(row, 5, QTableWidgetItem(t.description))
        
        self.table.resizeColumnsToContents()

    def refresh_table(self):
        txns = self.manager.get_transactions()
        self.table.setRowCount(len(txns))
        for row, t in enumerate(txns):
            self.table.setItem(row, 0, QTableWidgetItem(t.id))
            self.table.setItem(row, 1, QTableWidgetItem(t.date.strftime('%Y-%m-%d')))
            self.table.setItem(row, 2, QTableWidgetItem(t.type))
            self.table.setItem(row, 3, QTableWidgetItem(t.category))
            self.table.setItem(row, 4, QTableWidgetItem(f"₹{t.amount:.2f}"))
            self.table.setItem(row, 5, QTableWidgetItem(t.description))
        self.table.resizeColumnsToContents()

    def add_transaction(self):
        dlg = TransactionDialog(self.manager, self)
        if dlg.exec_():
            self.manager.add_transaction(
                dlg.amount(), dlg.type(), dlg.category(), dlg.description(), dlg.date()
            )
            self.refresh_table()

    def edit_transaction(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "No selection", "Please select a transaction to edit.")
            return
        item = self.table.item(row, 0)
        if item is None:
            QMessageBox.warning(self, "Not found", "Transaction not found.")
            return
        txn_id = item.text()
        txn = self.manager.get_transaction_by_id(txn_id)
        if not txn:
            QMessageBox.warning(self, "Not found", "Transaction not found.")
            return
        dlg = TransactionDialog(self.manager, self, txn)
        if dlg.exec_():
            self.manager.edit_transaction(
                txn.id,
                amount=dlg.amount(),
                type=dlg.type(),
                category=dlg.category(),
                description=dlg.description(),
                date=dlg.date()
            )
            self.refresh_table()

    def delete_transaction(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "No selection", "Please select a transaction to delete.")
            return
        item = self.table.item(row, 0)
        if item is None:
            QMessageBox.warning(self, "Not found", "Transaction not found.")
            return
        txn_id = item.text()
        if QMessageBox.question(self, "Confirm", "Delete this transaction?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.manager.delete_transaction(txn_id)
            self.refresh_table()
    
    def previous_page(self):
        """Go to the previous page of transactions."""
        if self._current_page > 0:
            self._current_page -= 1
            self.refresh_table()
    
    def next_page(self):
        """Go to the next page of transactions."""
        total_transactions = len(self.manager.get_transactions())
        max_pages = (total_transactions - 1) // self._page_size
        if self._current_page < max_pages:
            self._current_page += 1
            self.refresh_table()
    
    def _update_pagination_controls(self):
        """Update pagination controls based on current state."""
        total_transactions = len(self.manager.get_transactions())
        max_pages = (total_transactions - 1) // self._page_size
        
        self.prev_btn.setEnabled(self._current_page > 0)
        self.next_btn.setEnabled(self._current_page < max_pages)
        
        current_page_num = self._current_page + 1
        total_pages = max_pages + 1
        self.page_label.setText(f"Page {current_page_num} of {total_pages}")

class TransactionDialog(QDialog):
    def __init__(self, manager: BudgetManager, parent=None, txn=None):
        super().__init__(parent)
        self.manager = manager
        self.txn = txn
        self.setWindowTitle("Edit Transaction" if txn else "Add Transaction")
        self.setStyleSheet("background-color: white;")
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout(self)
        self.amount_edit = QLineEdit(str(self.txn.amount) if self.txn else "")
        self.type_combo = QComboBox()
        self.type_combo.addItems(["income", "expense", "transfer"])
        if self.txn:
            self.type_combo.setCurrentText(self.txn.type)
        self.category_combo = QComboBox()
        self.category_combo.addItems(self.manager.get_category_names())
        if self.txn:
            self.category_combo.setCurrentText(self.txn.category)
        self.desc_edit = QLineEdit(self.txn.description if self.txn else "")
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        from datetime import datetime
        if self.txn:
            self.date_edit.setDate(QDate(self.txn.date.year, self.txn.date.month, self.txn.date.day))
        else:
            today = datetime.now()
            self.date_edit.setDate(QDate(today.year, today.month, today.day))
        
        # Style the form elements
        self.amount_edit.setStyleSheet(MODERN_FORM_STYLE)
        self.type_combo.setStyleSheet(MODERN_FORM_STYLE)
        self.category_combo.setStyleSheet(MODERN_FORM_STYLE)
        self.desc_edit.setStyleSheet(MODERN_FORM_STYLE)
        self.date_edit.setStyleSheet(MODERN_FORM_STYLE)
        
        layout.addRow("Amount:", self.amount_edit)
        layout.addRow("Type:", self.type_combo)
        layout.addRow("Category:", self.category_combo)
        layout.addRow("Description:", self.desc_edit)
        layout.addRow("Date:", self.date_edit)
        btns = QHBoxLayout()
        ok_btn = QPushButton("OK")
        cancel_btn = QPushButton("Cancel")
        ok_btn.setStyleSheet(FALLBACK_BUTTON_STYLE)
        cancel_btn.setStyleSheet(FALLBACK_BUTTON_STYLE)
        ok_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        btns.addWidget(ok_btn)
        btns.addWidget(cancel_btn)
        layout.addRow(btns)

    def amount(self):
        val = self.amount_edit.text().strip()
        if not val:
            raise ValueError("Amount is required.")
        try:
            amount = float(val)
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            return amount
        except ValueError as e:
            if "must be positive" in str(e):
                raise e
            raise ValueError("Invalid amount. Please enter a valid number.")
    
    def type(self):
        return self.type_combo.currentText()
    
    def category(self):
        category = self.category_combo.currentText().strip()
        if not category:
            raise ValueError("Category is required.")
        return category
    def description(self):
        return self.desc_edit.text()
    def date(self):
        d = self.date_edit.date()
        from datetime import datetime
        return datetime(d.year(), d.month(), d.day())

class CategoriesWidget(QWidget):
    def __init__(self, manager: BudgetManager, parent=None):
        super().__init__(parent)
        self.manager = manager
        # Set white background
        self.setStyleSheet("background-color: white;")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Name", "Budget Limit", "Predefined"])
        self.table.setStyleSheet(MODERN_TABLE_STYLE)
        self.refresh_table()
        layout.addWidget(self.table)
        btn_layout = QHBoxLayout()
        add_btn = QPushButton("Add Category")
        edit_btn = QPushButton("Edit Selected")
        del_btn = QPushButton("Delete Selected")
        add_btn.setStyleSheet(FALLBACK_BUTTON_STYLE)
        edit_btn.setStyleSheet(FALLBACK_BUTTON_STYLE)
        del_btn.setStyleSheet(FALLBACK_BUTTON_STYLE)
        add_btn.clicked.connect(self.add_category)
        edit_btn.clicked.connect(self.edit_category)
        del_btn.clicked.connect(self.delete_category)
        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(edit_btn)
        btn_layout.addWidget(del_btn)
        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def refresh_table(self):
        cats = list(self.manager.categories.values())
        self.table.setRowCount(len(cats))
        for row, cat in enumerate(cats):
            self.table.setItem(row, 0, QTableWidgetItem(cat.name))
            self.table.setItem(row, 1, QTableWidgetItem(f"₹{cat.budget_limit:.2f}" if cat.budget_limit is not None else "No limit"))
            self.table.setItem(row, 2, QTableWidgetItem("Yes" if cat.is_predefined else "No"))
        self.table.resizeColumnsToContents()

    def add_category(self):
        dlg = CategoryDialog(self.manager, self)
        if dlg.exec_():
            try:
                self.manager.add_category(dlg.name(), dlg.budget_limit())
                self.refresh_table()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))

    def edit_category(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "No selection", "Please select a category to edit.")
            return
        item = self.table.item(row, 0)
        if item is None:
            QMessageBox.warning(self, "Not found", "Category not found.")
            return
        name = item.text()
        cat = self.manager.categories.get(name)
        if not cat:
            QMessageBox.warning(self, "Not found", "Category not found.")
            return
        dlg = CategoryDialog(self.manager, self, cat)
        if dlg.exec_():
            try:
                self.manager.edit_category(cat.name, new_name=dlg.name(), budget_limit=dlg.budget_limit())
                self.refresh_table()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))

    def delete_category(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "No selection", "Please select a category to delete.")
            return
        item = self.table.item(row, 0)
        if item is None:
            QMessageBox.warning(self, "Not found", "Category not found.")
            return
        name = item.text()
        if QMessageBox.question(self, "Confirm", "Delete this category?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            try:
                self.manager.delete_category(name)
                self.refresh_table()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))

class CategoryDialog(QDialog):
    def __init__(self, manager: BudgetManager, parent=None, cat=None):
        super().__init__(parent)
        self.manager = manager
        self.cat = cat
        self.setWindowTitle("Edit Category" if cat else "Add Category")
        self.setStyleSheet("background-color: white;")
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout(self)
        self.name_edit = QLineEdit(self.cat.name if self.cat else "")
        self.budget_edit = QLineEdit(str(self.cat.budget_limit) if self.cat and self.cat.budget_limit is not None else "")
        self.predefined_label = QLabel("Yes" if self.cat and self.cat.is_predefined else "No")
        
        # Style the form elements
        self.name_edit.setStyleSheet(MODERN_FORM_STYLE)
        self.budget_edit.setStyleSheet(MODERN_FORM_STYLE)
        
        layout.addRow("Name:", self.name_edit)
        layout.addRow("Budget Limit:", self.budget_edit)
        layout.addRow("Predefined:", self.predefined_label)
        btns = QHBoxLayout()
        ok_btn = QPushButton("OK")
        cancel_btn = QPushButton("Cancel")
        ok_btn.setStyleSheet(FALLBACK_BUTTON_STYLE)
        cancel_btn.setStyleSheet(FALLBACK_BUTTON_STYLE)
        ok_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        btns.addWidget(ok_btn)
        btns.addWidget(cancel_btn)
        layout.addRow(btns)

    def name(self):
        name = self.name_edit.text().strip()
        if not name:
            raise ValueError("Category name is required.")
        return name
    
    def budget_limit(self):
        val = self.budget_edit.text().strip()
        if not val:
            return None
        try:
            budget = float(val)
            if budget < 0:
                raise ValueError("Budget limit cannot be negative.")
            return budget
        except ValueError as e:
            if "cannot be negative" in str(e):
                raise e
            raise ValueError("Invalid budget limit. Please enter a valid number.")

class VisualizationsWidget(QWidget):
    def __init__(self, manager: BudgetManager, parent=None):
        super().__init__(parent)
        self.manager = manager
        # Set white background
        self.setStyleSheet("background-color: white;")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Data Visualizations")
        title.setStyleSheet("font-size: 24px; font-weight: 600; margin-bottom: 20px; color: #2c3e50; font-family: 'Segoe UI', Arial, sans-serif;")
        layout.addWidget(title, alignment=get_alignment())
        
        # Chart buttons in a grid layout
        button_layout = QHBoxLayout()
        
        pie_btn = QPushButton("📊 Expense Breakdown\n(Pie Chart)")
        bar_btn = QPushButton("📈 Monthly Expenses\n(Bar Chart)")
        trend_btn = QPushButton("📉 Expense Trends\n(Line Chart)")
        budget_btn = QPushButton("💰 Budget vs Actual\n(Comparison)")
        
        # Style buttons
        for btn in [pie_btn, bar_btn, trend_btn, budget_btn]:
            btn.setStyleSheet(FALLBACK_BUTTON_STYLE)
            btn.setMinimumHeight(80)
            btn.setMinimumWidth(150)
        
        # Connect buttons
        pie_btn.clicked.connect(self.show_pie_chart)
        bar_btn.clicked.connect(self.show_bar_chart)
        trend_btn.clicked.connect(self.show_trend_chart)
        budget_btn.clicked.connect(self.show_budget_comparison)
        
        button_layout.addWidget(pie_btn)
        button_layout.addWidget(bar_btn)
        button_layout.addWidget(trend_btn)
        button_layout.addWidget(budget_btn)
        
        layout.addLayout(button_layout)
        layout.addStretch()
        self.setLayout(layout)

    def show_pie_chart(self):
        from datetime import datetime
        now = datetime.now()
        summary = self.manager.get_monthly_summary(now.year, now.month)
        category_data = summary['category_breakdown']
        labels = []
        sizes = []
        for cat, vals in category_data.items():
            if vals.get('expense', 0) > 0:
                labels.append(cat)
                sizes.append(vals['expense'])
        if not sizes:
            QMessageBox.information(self, "No Data", "No expenses to visualize for this month.")
            return
        win = QDialog(self)
        win.setWindowTitle("Expense Breakdown (Pie Chart)")
        win.showMaximized()  # Open in fullscreen
        win.setStyleSheet("background-color: white;")
        
        # Use large figure size for better visibility
        fig, ax = plt.subplots(figsize=(16, 12))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        ax.set_title(f"Expense Breakdown by Category\n{now.year}-{now.month:02d}", fontsize=16, fontweight='bold')
        canvas = FigureCanvas(fig)
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        win.setLayout(layout)
        win.exec_()

    def show_bar_chart(self):
        from datetime import datetime
        now = datetime.now()
        summary = self.manager.get_monthly_summary(now.year, now.month)
        category_data = summary['category_breakdown']
        labels = []
        sizes = []
        for cat, vals in category_data.items():
            if vals.get('expense', 0) > 0:
                labels.append(cat)
                sizes.append(vals['expense'])
        if not sizes:
            QMessageBox.information(self, "No Data", "No expenses to visualize for this month.")
            return
        win = QDialog(self)
        win.setWindowTitle("Monthly Expenses by Category (Bar Chart)")
        win.showMaximized()  # Open in fullscreen
        win.setStyleSheet("background-color: white;")
        
        # Use large figure size for better visibility
        fig, ax = plt.subplots(figsize=(16, 12))
        bars = ax.bar(labels, sizes, color='skyblue', edgecolor='navy', linewidth=1)
        ax.set_ylabel('Amount (₹)', fontsize=14, fontweight='bold')
        ax.set_xlabel('Category', fontsize=14, fontweight='bold')
        ax.set_title(f"Monthly Expenses by Category\n{now.year}-{now.month:02d}", fontsize=16, fontweight='bold')
        ax.tick_params(axis='x', rotation=30, labelsize=12)
        ax.tick_params(axis='y', labelsize=12)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + max(sizes)*0.01,
                   f"₹{height:.2f}", ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        fig.tight_layout()
        canvas = FigureCanvas(fig)
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        win.setLayout(layout)
        win.exec_()

    def show_trend_chart(self):
        from datetime import datetime
        now = datetime.now()
        # Assuming you have a method to get historical data or need to fetch it
        # For now, let's use a placeholder or fetch recent data
        # This part would require a more robust data fetching mechanism
        # For demonstration, let's use a dummy list of dates and amounts
        dummy_dates = [
            datetime(2023, 1, 1), datetime(2023, 2, 1), datetime(2023, 3, 1),
            datetime(2023, 4, 1), datetime(2023, 5, 1), datetime(2023, 6, 1),
            datetime(2023, 7, 1), datetime(2023, 8, 1), datetime(2023, 9, 1),
            datetime(2023, 10, 1), datetime(2023, 11, 1), datetime(2023, 12, 1)
        ]
        dummy_amounts = [
            1000, 1200, 1100, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100
        ]

        if len(dummy_dates) < 2:
            QMessageBox.information(self, "Not Enough Data", "Need at least two data points for a trend chart.")
            return

        win = QDialog(self)
        win.setWindowTitle("Expense Trends (Line Chart)")
        win.showMaximized()  # Open in fullscreen
        win.setStyleSheet("background-color: white;")
        
        # Use large figure size for better visibility
        fig, ax = plt.subplots(figsize=(16, 12))
        # Convert datetime objects to matplotlib dates
        dates_mpl = mdates.date2num(dummy_dates)
        ax.plot(dates_mpl, dummy_amounts, marker='o', linestyle='-', color='blue', linewidth=3, markersize=8)
        ax.set_ylabel('Amount (₹)', fontsize=14, fontweight='bold')
        ax.set_xlabel('Date', fontsize=14, fontweight='bold')
        ax.set_title(f"Monthly Expense Trends\n{now.year}", fontsize=16, fontweight='bold')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        ax.tick_params(axis='x', rotation=45, labelsize=12)
        ax.tick_params(axis='y', labelsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)
        fig.tight_layout()
        canvas = FigureCanvas(fig)
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        win.setLayout(layout)
        win.exec_()

    def show_budget_comparison(self):
        from datetime import datetime
        now = datetime.now()
        
        # Get category performance data
        performance = self.manager.get_category_performance(now.year, now.month)
        
        if not performance:
            QMessageBox.information(self, "No Data", "No budget data available for comparison.")
            return
        
        # Prepare data for comparison - only include categories with budget limits
        categories_with_budgets = {cat: data for cat, data in performance.items() 
                                 if data['budget_limit'] is not None and data['status'] != 'no_budget_set'}
        
        if not categories_with_budgets:
            QMessageBox.information(self, "No Budget Data", "No categories with budget limits found. Set budget limits in Categories section.")
            return
        
        categories = list(categories_with_budgets.keys())
        budget_amounts = [categories_with_budgets[cat]['budget_limit'] for cat in categories]
        actual_amounts = [categories_with_budgets[cat]['expense'] for cat in categories]

        win = QDialog(self)
        win.setWindowTitle("Budget vs Actual Comparison")
        win.showMaximized()  # Open in fullscreen
        win.setStyleSheet("background-color: white;")
        
        # Use large figure size for better visibility
        fig, ax = plt.subplots(figsize=(16, 12))
        bar_width = 0.35
        index = np.arange(len(categories))

        budget_bars = ax.bar(index - bar_width/2, budget_amounts, bar_width, label='Budget', color='lightgreen', edgecolor='darkgreen', linewidth=1)
        actual_bars = ax.bar(index + bar_width/2, actual_amounts, bar_width, label='Actual', color='lightcoral', edgecolor='darkred', linewidth=1)

        ax.set_ylabel('Amount (₹)', fontsize=14, fontweight='bold')
        ax.set_xlabel('Categories', fontsize=14, fontweight='bold')
        ax.set_title(f"Budget vs Actual Expenses\n{now.year}-{now.month:02d}", fontsize=16, fontweight='bold')
        ax.set_xticks(index)
        ax.set_xticklabels(categories, fontsize=12)
        ax.tick_params(axis='y', labelsize=12)
        ax.legend(fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)
        fig.tight_layout()
        canvas = FigureCanvas(fig)
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        win.setLayout(layout)
        win.exec_()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Personal Finance Tracker (PyQt)")
        # Make app open in maximized state by default
        self.showMaximized()
        # Set white background for main window
        self.setStyleSheet("background-color: white;")
        self.manager = BudgetManager()
        self.init_ui()

    def init_ui(self):
        # Navigation
        nav_widget = QWidget()
        nav_layout = QHBoxLayout()
        nav_widget.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1e293b, stop:1 #334155); 
                border-bottom: 3px solid #475569;
                padding: 8px;
            }
        """)
        
        # Main navigation buttons
        self.btn_dashboard = QPushButton("Dashboard")
        self.btn_transactions = QPushButton("Transactions")
        self.btn_categories = QPushButton("Categories")
        self.btn_visualizations = QPushButton("Visualizations")
        
        # Export/Import buttons as separate buttons
        self.btn_export_csv = QPushButton("Export CSV")
        self.btn_export_json = QPushButton("Export JSON")
        self.btn_import_csv = QPushButton("Import CSV")
        self.btn_import_json = QPushButton("Import JSON")
        
        # Action buttons
        self.btn_settings = QPushButton("⚙️ Settings")
        self.btn_clear_expenses = QPushButton("Clear All Expenses")
        
        # Ensure buttons are visible
        self.btn_dashboard.setVisible(True)
        self.btn_transactions.setVisible(True)
        self.btn_categories.setVisible(True)
        self.btn_visualizations.setVisible(True)
        self.btn_export_csv.setVisible(True)
        self.btn_export_json.setVisible(True)
        self.btn_import_csv.setVisible(True)
        self.btn_import_json.setVisible(True)
        self.btn_settings.setVisible(True)
        self.btn_clear_expenses.setVisible(True)
        
        # Apply navigation button styling
        self.btn_dashboard.setStyleSheet(NAV_BUTTON_STYLE)
        self.btn_transactions.setStyleSheet(NAV_BUTTON_STYLE)
        self.btn_categories.setStyleSheet(NAV_BUTTON_STYLE)
        self.btn_visualizations.setStyleSheet(NAV_BUTTON_STYLE)
        
        # Apply export/import button styling
        self.btn_export_csv.setStyleSheet(SUBMENU_BUTTON_STYLE)
        self.btn_export_json.setStyleSheet(SUBMENU_BUTTON_STYLE)
        self.btn_import_csv.setStyleSheet(SUBMENU_BUTTON_STYLE)
        self.btn_import_json.setStyleSheet(SUBMENU_BUTTON_STYLE)
        
        # Apply action button styling
        self.btn_settings.setStyleSheet(SETTINGS_BUTTON_STYLE)
        self.btn_clear_expenses.setStyleSheet(FALLBACK_CLEAR_BUTTON_STYLE)
        
        # Set initial active state
        self.active_button = self.btn_dashboard
        self.update_active_button(self.btn_dashboard)
        
        # Connect export/import buttons to their functions
        self.btn_export_csv.clicked.connect(self.export_csv)
        self.btn_export_json.clicked.connect(self.export_json)
        self.btn_import_csv.clicked.connect(self.import_csv)
        self.btn_import_json.clicked.connect(self.import_json)
        
        # Layout organization - Simple horizontal layout
        nav_layout.addWidget(self.btn_dashboard)
        nav_layout.addWidget(self.btn_transactions)
        nav_layout.addWidget(self.btn_categories)
        nav_layout.addWidget(self.btn_visualizations)
        nav_layout.addStretch()
        nav_layout.addWidget(self.btn_export_csv)
        nav_layout.addWidget(self.btn_export_json)
        nav_layout.addWidget(self.btn_import_csv)
        nav_layout.addWidget(self.btn_import_json)
        nav_layout.addWidget(self.btn_settings)
        nav_layout.addWidget(self.btn_clear_expenses)
        nav_widget.setLayout(nav_layout)
        
        # Stacked pages
        self.stacked = QStackedWidget()
        self.dashboard_page = DashboardWidget(self.manager)
        self.stacked.addWidget(self.dashboard_page)
        # Transactions page
        self.transactions_page = TransactionsWidget(self.manager)
        self.stacked.addWidget(self.transactions_page)
        # Categories page
        self.categories_page = CategoriesWidget(self.manager)
        self.stacked.addWidget(self.categories_page)
        # Visualizations page
        self.visualizations_page = VisualizationsWidget(self.manager)
        self.stacked.addWidget(self.visualizations_page)
        # Main layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(nav_widget)
        main_layout.addWidget(self.stacked)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        # Navigation actions
        self.btn_dashboard.clicked.connect(lambda: self.navigate_to_page(self.dashboard_page, self.btn_dashboard))
        self.btn_transactions.clicked.connect(lambda: self.navigate_to_page(self.transactions_page, self.btn_transactions))
        self.btn_categories.clicked.connect(lambda: self.navigate_to_page(self.categories_page, self.btn_categories))
        self.btn_visualizations.clicked.connect(lambda: self.navigate_to_page(self.visualizations_page, self.btn_visualizations))
        self.btn_clear_expenses.clicked.connect(self.dashboard_page.clear_expenses)
        self.btn_settings.clicked.connect(self.show_settings_dialog) # Connect settings button
    
    def navigate_to_page(self, page, button):
        """Navigate to a page and update active button styling."""
        self.stacked.setCurrentWidget(page)
        self.update_active_button(button)
    
    def update_active_button(self, active_button):
        """Update the active button styling."""
        # Reset all buttons to normal style
        for button in [self.btn_dashboard, self.btn_transactions, self.btn_categories, self.btn_visualizations]:
            button.setStyleSheet(NAV_BUTTON_STYLE)
        
        # Set active button style
        active_style = """
        QPushButton {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #dc2626, stop:1 #b91c1c);
            border: 1px solid #991b1b;
            border-radius: 6px;
            color: white;
            font-weight: 600;
            padding: 12px 20px;
            font-size: 14px;
            margin: 2px;
            font-family: 'Segoe UI', Arial, sans-serif;
        }
        QPushButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #dc2626, stop:1 #b91c1c);
        }
        """
        active_button.setStyleSheet(active_style)
        self.active_button = active_button
    
    def export_csv(self):
        """Export data to CSV format."""
        try:
            filepath = self.manager.export_data("csv")
            QMessageBox.information(self, "Export Successful", f"Data exported to:\n{filepath}")
        except Exception as e:
            QMessageBox.warning(self, "Export Failed", f"Failed to export data: {str(e)}")
    
    def export_json(self):
        """Export data to JSON format."""
        try:
            filepath = self.manager.export_data("json")
            QMessageBox.information(self, "Export Successful", f"Data exported to:\n{filepath}")
        except Exception as e:
            QMessageBox.warning(self, "Export Failed", f"Failed to export data: {str(e)}")
    
    def import_csv(self):
        """Import data from CSV file."""
        filepath, _ = QFileDialog.getOpenFileName(self, "Import CSV Data", "", "CSV Files (*.csv);;All Files (*)")
        if filepath:
            try:
                self.manager.import_data(filepath, "csv")
                QMessageBox.information(self, "Import Successful", f"Data imported from:\n{filepath}")
                self.refresh_all_widgets() # Refresh all widgets to show new data
            except Exception as e:
                QMessageBox.warning(self, "Import Failed", f"Failed to import data: {str(e)}")
    
    def import_json(self):
        """Import data from JSON file."""
        filepath, _ = QFileDialog.getOpenFileName(self, "Import JSON Data", "", "JSON Files (*.json);;All Files (*)")
        if filepath:
            try:
                self.manager.import_data(filepath, "json")
                QMessageBox.information(self, "Import Successful", f"Data imported from:\n{filepath}")
                self.refresh_all_widgets() # Refresh all widgets to show new data
            except Exception as e:
                QMessageBox.warning(self, "Import Failed", f"Failed to import data: {str(e)}")
    
    def refresh_all_widgets(self):
        """Refresh all widgets in the main window to show updated data."""
        self.dashboard_page.refresh_dashboard()
        self.transactions_page.refresh_table()
        self.categories_page.refresh_table()
        # No direct refresh for VisualizationsWidget as it's a button-driven page
    
    def closeEvent(self, event):
        # Clean exit
        event.accept()

    def show_settings_dialog(self):
        """Show the settings dialog."""
        dialog = SettingsDialog(self)
        if dialog.exec_():
            # Apply settings if dialog was accepted
            self.apply_settings(dialog.get_settings())
    
    def apply_settings(self, settings):
        """Apply the selected settings."""
        # This is where you would apply the settings to the application
        # For now, just show a message
        QMessageBox.information(self, "Settings Applied", "Settings have been applied successfully!")


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setModal(True)
        self.resize(400, 300)
        self.setStyleSheet("background-color: white;")
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Application Settings")
        title.setStyleSheet("font-size: 20px; font-weight: 600; margin-bottom: 20px; color: #2c3e50; font-family: 'Segoe UI', Arial, sans-serif;")
        layout.addWidget(title, alignment=get_alignment())
        
        # Settings form
        form_layout = QFormLayout()
        
        # Currency symbol
        self.currency_combo = QComboBox()
        self.currency_combo.addItems(["₹ (INR)", "$ (USD)", "€ (EUR)", "£ (GBP)"])
        self.currency_combo.setCurrentText("₹ (INR)")
        self.currency_combo.setStyleSheet(MODERN_FORM_STYLE)
        form_layout.addRow("Currency:", self.currency_combo)
        
        # Date format
        self.date_format_combo = QComboBox()
        self.date_format_combo.addItems(["YYYY-MM-DD", "DD/MM/YYYY", "MM/DD/YYYY"])
        self.date_format_combo.setCurrentText("YYYY-MM-DD")
        self.date_format_combo.setStyleSheet(MODERN_FORM_STYLE)
        form_layout.addRow("Date Format:", self.date_format_combo)
        
        # Theme
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Light", "Dark", "Auto"])
        self.theme_combo.setCurrentText("Light")
        self.theme_combo.setStyleSheet(MODERN_FORM_STYLE)
        form_layout.addRow("Theme:", self.theme_combo)
        
        # Auto-save
        self.auto_save_checkbox = QCheckBox("Auto-save changes")
        self.auto_save_checkbox.setChecked(True)
        self.auto_save_checkbox.setStyleSheet("""
            QCheckBox {
                font-family: 'Segoe UI', Arial, sans-serif;
                font-size: 14px;
                color: #495057;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #dee2e6;
                border-radius: 4px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #667eea;
                border-color: #667eea;
            }
        """)
        form_layout.addRow("", self.auto_save_checkbox)
        
        layout.addLayout(form_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        ok_btn = QPushButton("OK")
        cancel_btn = QPushButton("Cancel")
        reset_btn = QPushButton("Reset to Defaults")
        
        ok_btn.setStyleSheet(FALLBACK_BUTTON_STYLE)
        cancel_btn.setStyleSheet(FALLBACK_BUTTON_STYLE)
        reset_btn.setStyleSheet(FALLBACK_BUTTON_STYLE)
        
        ok_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        reset_btn.clicked.connect(self.reset_to_defaults)
        
        button_layout.addWidget(reset_btn)
        button_layout.addStretch()
        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(ok_btn)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def get_settings(self):
        """Get the current settings."""
        return {
            'currency': self.currency_combo.currentText(),
            'date_format': self.date_format_combo.currentText(),
            'theme': self.theme_combo.currentText(),
            'auto_save': self.auto_save_checkbox.isChecked()
        }
    
    def reset_to_defaults(self):
        """Reset settings to default values."""
        self.currency_combo.setCurrentText("₹ (INR)")
        self.date_format_combo.setCurrentText("YYYY-MM-DD")
        self.theme_combo.setCurrentText("Light")
        self.auto_save_checkbox.setChecked(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 