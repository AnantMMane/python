import uuid
from datetime import datetime
from typing import Literal, Optional


class Transaction:
    """
    Represents a financial transaction (income, expense, or transfer).
    
    Attributes:
        id (str): Unique identifier for the transaction
        amount (float): Positive amount in INR
        type (str): 'income', 'expense', or 'transfer'
        category (str): Category of the transaction
        description (str): Description or note for the transaction
        date (datetime): Date of the transaction (ISO format)
        currency (str): Currency code (default: INR)
    """
    
    def __init__(
        self,
        amount: float,
        type: Literal["income", "expense", "transfer"],
        category: str,
        description: str = "",
        date: datetime | None = None,
        currency: str = "INR",
        id: str | None = None
    ):
        if type not in ("income", "expense", "transfer"):
            raise ValueError("Transaction type must be 'income', 'expense', or 'transfer'")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if not category or not category.strip():
            raise ValueError("Category must be specified")
        
        self.id = id if id else str(uuid.uuid4())
        self.amount = amount
        self.type = type
        self.category = category.strip()
        self.description = description
        self.date = date if date else datetime.now()
        self.currency = currency
    
    def __str__(self) -> str:
        """String representation of the transaction."""
        return f"{self.date.strftime('%Y-%m-%d')} | {self.type.upper()} | {self.category} | ₹{self.amount:.2f} | {self.description}"
    
    def __repr__(self) -> str:
        """Detailed string representation for debugging."""
        return f"Transaction(id={self.id}, amount={self.amount}, type={self.type}, category={self.category}, date={self.date})"
    
    def to_dict(self) -> dict:
        """Convert transaction to dictionary for CSV storage."""
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d'),
            'amount': self.amount,
            'type': self.type,
            'category': self.category,
            'description': self.description,
            'currency': self.currency
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Transaction':
        """Create transaction from dictionary (for loading from CSV)."""
        return cls(
            amount=float(data['amount']),
            type=data['type'],
            category=data['category'],
            description=data.get('description', ''),
            date=datetime.strptime(data['date'], '%Y-%m-%d'),
            currency=data.get('currency', 'INR'),
            id=data.get('id')
        )
    
    def update_fields(self, amount: Optional[float] = None, type: Optional[str] = None, category: Optional[str] = None, description: Optional[str] = None, date: Optional[datetime] = None, currency: Optional[str] = None):
        """Update transaction fields for editing."""
        if amount is not None:
            if amount <= 0:
                raise ValueError("Amount must be positive")
            self.amount = amount
        if type is not None:
            if type not in ("income", "expense", "transfer"):
                raise ValueError("Transaction type must be 'income', 'expense', or 'transfer'")
            self.type = type
        if category is not None:
            if not category or not category.strip():
                raise ValueError("Category must be specified")
            self.category = category.strip()
        if description is not None:
            self.description = description
        if date is not None:
            self.date = date
        if currency is not None:
            self.currency = currency
    
    def get_display_amount(self) -> str:
        """Get formatted amount with currency symbol."""
        return f"₹{self.amount:.2f}"
    
    def is_income(self) -> bool:
        """Check if transaction is income."""
        return self.type == "income"
    
    def is_expense(self) -> bool:
        """Check if transaction is expense."""
        return self.type == "expense"
    
    def is_transfer(self) -> bool:
        """Check if transaction is transfer."""
        return self.type == "transfer" 