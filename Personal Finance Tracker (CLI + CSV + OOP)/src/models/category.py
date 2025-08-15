from typing import Optional


class Category:
    """
    Represents a category for transactions with optional budget limit.
    
    Attributes:
        name (str): Name of the category
        budget_limit (Optional[float]): Monthly budget limit in INR (None if no limit)
        is_predefined (bool): Whether this is a predefined category
    """
    
    # Predefined categories
    PREDEFINED_CATEGORIES = {
        "Food": None,
        "Rent": None,
        "Salary": None,
        "Miscellaneous Expenses": None,
        "Transportation": None,
        "Utilities": None,
        "Entertainment": None,
        "Healthcare": None,
        "Shopping": None,
        "Education": None,
        "Investment": None,
        "Transfer": None
    }
    
    def __init__(self, name: str, budget_limit: Optional[float] = None, is_predefined: bool = False):
        if not name or not name.strip():
            raise ValueError("Category name must be non-empty")
        self.name = name.strip()  # Normalize the name
        
        # Validate budget limit if provided
        if budget_limit is not None and budget_limit < 0:
            raise ValueError("Budget limit cannot be negative")
        
        self.budget_limit = budget_limit
        self.is_predefined = bool(is_predefined)
    
    def __str__(self) -> str:
        """String representation of the category."""
        budget_info = f" (Budget: ₹{self.budget_limit:.2f})" if self.budget_limit else ""
        return f"{self.name}{budget_info}"
    
    def __repr__(self) -> str:
        """Detailed string representation for debugging."""
        return f"Category(name='{self.name}', budget_limit={self.budget_limit}, is_predefined={self.is_predefined})"
    
    def to_dict(self) -> dict:
        """Convert category to dictionary for CSV storage."""
        return {
            'name': self.name,
            'budget_limit': self.budget_limit if self.budget_limit else '',
            'is_predefined': self.is_predefined
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Category':
        """Create category from dictionary (for loading from CSV)."""
        budget_limit = float(data['budget_limit']) if data.get('budget_limit') else None
        is_predefined = data.get('is_predefined', False)
        if isinstance(is_predefined, str):
            is_predefined = is_predefined.lower() in ("true", "1", "yes")
        return cls(
            name=data['name'],
            budget_limit=budget_limit,
            is_predefined=is_predefined
        )
    
    @classmethod
    def get_predefined_categories(cls) -> list['Category']:
        """Get list of all predefined categories."""
        return [
            Category(name=name, budget_limit=budget_limit, is_predefined=True)
            for name, budget_limit in cls.PREDEFINED_CATEGORIES.items()
        ]
    
    @classmethod
    def is_predefined_category(cls, name: str) -> bool:
        """Check if a category name is predefined."""
        return name in cls.PREDEFINED_CATEGORIES
    
    def has_budget_limit(self) -> bool:
        """Check if category has a budget limit set."""
        return self.budget_limit is not None
    
    def set_budget_limit(self, limit: float) -> None:
        """Set or update the budget limit for this category."""
        if limit < 0:
            raise ValueError("Budget limit cannot be negative")
        self.budget_limit = limit
    
    def remove_budget_limit(self) -> None:
        """Remove the budget limit for this category."""
        self.budget_limit = None
    
    def get_budget_display(self) -> str:
        """Get formatted budget limit with currency symbol."""
        if self.budget_limit:
            return f"₹{self.budget_limit:.2f}"
        return "No limit" 

    def update_fields(self, name: Optional[str] = None, budget_limit: Optional[float] = None):
        """Update category fields for editing."""
        if name is not None:
            if not name.strip():
                raise ValueError("Category name must be non-empty")
            self.name = name.strip()
        if budget_limit is not None:
            if budget_limit < 0:
                raise ValueError("Budget limit cannot be negative")
            self.budget_limit = budget_limit 