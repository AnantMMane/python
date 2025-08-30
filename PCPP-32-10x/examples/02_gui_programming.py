#!/usr/bin/env python3
"""
GUI Programming with tkinter Examples
PCPP Certification Study Material

This module demonstrates tkinter GUI programming concepts including:
- Basic window and widget creation
- Layout management (pack, grid, place)
- Event handling
- Custom widgets
- Advanced components (Treeview, Canvas)
- Model-View-Controller pattern
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
from datetime import datetime


# 1. Basic Application Structure
class BasicApplication:
    """Basic tkinter application template"""
    
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_widgets()
        self.arrange_widgets()
        self.bind_events()
    
    def setup_window(self):
        """Configure the main window"""
        self.root.title("Basic Tkinter Application")
        self.root.geometry("400x300")
        self.root.minsize(300, 200)
        
        # Center window on screen
        self.center_window()
    
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def create_widgets(self):
        """Create all widgets"""
        # Title label
        self.title_label = ttk.Label(
            self.root, 
            text="Welcome to Tkinter!", 
            font=("Arial", 16, "bold")
        )
        
        # Input frame
        self.input_frame = ttk.Frame(self.root)
        
        # Entry with label
        self.name_label = ttk.Label(self.input_frame, text="Your Name:")
        self.name_entry = ttk.Entry(self.input_frame, width=20)
        
        # Buttons frame
        self.button_frame = ttk.Frame(self.root)
        
        self.greet_button = ttk.Button(
            self.button_frame, 
            text="Greet", 
            command=self.greet_user
        )
        
        self.clear_button = ttk.Button(
            self.button_frame, 
            text="Clear", 
            command=self.clear_entry
        )
        
        self.quit_button = ttk.Button(
            self.button_frame, 
            text="Quit", 
            command=self.root.quit
        )
        
        # Output text widget
        self.output_text = tk.Text(
            self.root, 
            height=8, 
            width=40, 
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        
        # Scrollbar for text widget
        self.scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.output_text.yview)
        self.output_text.config(yscrollcommand=self.scrollbar.set)
    
    def arrange_widgets(self):
        """Arrange widgets using layout managers"""
        # Title
        self.title_label.pack(pady=10)
        
        # Input frame
        self.input_frame.pack(pady=5)
        self.name_label.pack(side=tk.LEFT, padx=5)
        self.name_entry.pack(side=tk.LEFT, padx=5)
        
        # Buttons frame
        self.button_frame.pack(pady=10)
        self.greet_button.pack(side=tk.LEFT, padx=5)
        self.clear_button.pack(side=tk.LEFT, padx=5)
        self.quit_button.pack(side=tk.LEFT, padx=5)
        
        # Output text with scrollbar
        text_frame = ttk.Frame(self.root)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def bind_events(self):
        """Bind keyboard and mouse events"""
        self.name_entry.bind('<Return>', lambda e: self.greet_user())
        self.name_entry.bind('<Escape>', lambda e: self.clear_entry())
        self.root.bind('<Control-q>', lambda e: self.root.quit())
    
    def greet_user(self):
        """Greet the user with entered name"""
        name = self.name_entry.get().strip()
        if name:
            timestamp = datetime.now().strftime("%H:%M:%S")
            message = f"[{timestamp}] Hello, {name}! Welcome to tkinter programming.\n"
            self.append_to_output(message)
        else:
            messagebox.showwarning("Warning", "Please enter your name!")
    
    def clear_entry(self):
        """Clear the name entry"""
        self.name_entry.delete(0, tk.END)
        self.name_entry.focus()
    
    def append_to_output(self, text):
        """Append text to output widget"""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, text)
        self.output_text.see(tk.END)
        self.output_text.config(state=tk.DISABLED)


# 2. Custom Widgets
class LabeledEntry(ttk.Frame):
    """Custom widget combining label and entry"""
    
    def __init__(self, parent, label_text, entry_width=20, **kwargs):
        super().__init__(parent)
        
        self.label = ttk.Label(self, text=label_text)
        self.entry = ttk.Entry(self, width=entry_width, **kwargs)
        
        self.label.pack(side=tk.LEFT, padx=(0, 5))
        self.entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
    
    def get(self):
        """Get entry value"""
        return self.entry.get()
    
    def set(self, value):
        """Set entry value"""
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(value))
    
    def clear(self):
        """Clear entry"""
        self.entry.delete(0, tk.END)
    
    def focus(self):
        """Focus on entry"""
        self.entry.focus()


class StatusBar(ttk.Frame):
    """Custom status bar widget"""
    
    def __init__(self, parent):
        super().__init__(parent, relief=tk.SUNKEN, borderwidth=1)
        
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        
        self.status_label = ttk.Label(self, textvariable=self.status_var)
        self.status_label.pack(side=tk.LEFT, padx=5, pady=2)
        
        self.progress = ttk.Progressbar(self, length=200, mode='determinate')
        self.progress.pack(side=tk.RIGHT, padx=5, pady=2)
    
    def set_status(self, text):
        """Set status text"""
        self.status_var.set(text)
    
    def set_progress(self, value):
        """Set progress bar value (0-100)"""
        self.progress['value'] = value
    
    def start_progress(self):
        """Start indeterminate progress"""
        self.progress.config(mode='indeterminate')
        self.progress.start()
    
    def stop_progress(self):
        """Stop progress and reset"""
        self.progress.stop()
        self.progress.config(mode='determinate')
        self.progress['value'] = 0


# 3. Advanced Components Example
class DataManagerApp:
    """Advanced GUI application demonstrating various tkinter components"""
    
    def __init__(self, root):
        self.root = root
        self.data = []
        self.setup_window()
        self.create_menu()
        self.create_widgets()
        self.arrange_widgets()
        self.load_sample_data()
    
    def setup_window(self):
        """Setup main window"""
        self.root.title("Data Manager - Advanced Tkinter Example")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
    
    def create_menu(self):
        """Create menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Add Item", command=self.add_item)
        edit_menu.add_command(label="Edit Item", command=self.edit_item)
        edit_menu.add_command(label="Delete Item", command=self.delete_item)
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Refresh", command=self.refresh_view)
        
        # Bind keyboard shortcuts
        self.root.bind('<Control-n>', lambda e: self.new_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())
    
    def create_widgets(self):
        """Create all widgets"""
        # Main container
        self.main_frame = ttk.Frame(self.root)
        
        # Toolbar
        self.toolbar = ttk.Frame(self.main_frame)
        
        self.add_btn = ttk.Button(self.toolbar, text="Add", command=self.add_item)
        self.edit_btn = ttk.Button(self.toolbar, text="Edit", command=self.edit_item)
        self.delete_btn = ttk.Button(self.toolbar, text="Delete", command=self.delete_item)
        self.refresh_btn = ttk.Button(self.toolbar, text="Refresh", command=self.refresh_view)
        
        # Search frame
        self.search_frame = ttk.Frame(self.main_frame)
        self.search_label = ttk.Label(self.search_frame, text="Search:")\n        self.search_var = tk.StringVar()\n        self.search_entry = ttk.Entry(self.search_frame, textvariable=self.search_var)\n        self.search_var.trace('w', self.filter_data)\n        \n        # Data display - Treeview\n        self.tree_frame = ttk.Frame(self.main_frame)\n        \n        # Define columns\n        columns = ('ID', 'Name', 'Category', 'Price', 'Quantity')\n        self.tree = ttk.Treeview(self.tree_frame, columns=columns, show='headings', height=15)\n        \n        # Define headings\n        for col in columns:\n            self.tree.heading(col, text=col, command=lambda c=col: self.sort_by_column(c))\n            self.tree.column(col, width=120, anchor=tk.CENTER)\n        \n        # Scrollbars for treeview\n        self.v_scrollbar = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL, command=self.tree.yview)\n        self.h_scrollbar = ttk.Scrollbar(self.tree_frame, orient=tk.HORIZONTAL, command=self.tree.xview)\n        self.tree.configure(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)\n        \n        # Bind treeview events\n        self.tree.bind('<Double-1>', lambda e: self.edit_item())\n        self.tree.bind('<Delete>', lambda e: self.delete_item())\n        \n        # Status bar\n        self.status_bar = StatusBar(self.main_frame)\n    \n    def arrange_widgets(self):\n        \"\"\"Arrange widgets using grid layout\"\"\"\n        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)\n        \n        # Toolbar\n        self.toolbar.pack(fill=tk.X, pady=(0, 5))\n        self.add_btn.pack(side=tk.LEFT, padx=2)\n        self.edit_btn.pack(side=tk.LEFT, padx=2)\n        self.delete_btn.pack(side=tk.LEFT, padx=2)\n        self.refresh_btn.pack(side=tk.LEFT, padx=2)\n        \n        # Search frame\n        self.search_frame.pack(fill=tk.X, pady=(0, 5))\n        self.search_label.pack(side=tk.LEFT, padx=(0, 5))\n        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)\n        \n        # Treeview frame\n        self.tree_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 5))\n        \n        # Grid layout for treeview and scrollbars\n        self.tree.grid(row=0, column=0, sticky='nsew')\n        self.v_scrollbar.grid(row=0, column=1, sticky='ns')\n        self.h_scrollbar.grid(row=1, column=0, sticky='ew')\n        \n        # Configure grid weights\n        self.tree_frame.grid_rowconfigure(0, weight=1)\n        self.tree_frame.grid_columnconfigure(0, weight=1)\n        \n        # Status bar\n        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)\n    \n    def load_sample_data(self):\n        \"\"\"Load sample data into the application\"\"\"\n        sample_data = [\n            {\"id\": 1, \"name\": \"Laptop\", \"category\": \"Electronics\", \"price\": 999.99, \"quantity\": 10},\n            {\"id\": 2, \"name\": \"Mouse\", \"category\": \"Electronics\", \"price\": 29.99, \"quantity\": 50},\n            {\"id\": 3, \"name\": \"Keyboard\", \"category\": \"Electronics\", \"price\": 79.99, \"quantity\": 25},\n            {\"id\": 4, \"name\": \"Monitor\", \"category\": \"Electronics\", \"price\": 299.99, \"quantity\": 15},\n            {\"id\": 5, \"name\": \"Desk Chair\", \"category\": \"Furniture\", \"price\": 149.99, \"quantity\": 8},\n        ]\n        \n        self.data = sample_data\n        self.refresh_view()\n    \n    def refresh_view(self):\n        \"\"\"Refresh the treeview with current data\"\"\"\n        # Clear existing items\n        for item in self.tree.get_children():\n            self.tree.delete(item)\n        \n        # Filter data based on search\n        search_term = self.search_var.get().lower()\n        filtered_data = []\n        \n        for item in self.data:\n            if (search_term in item['name'].lower() or \n                search_term in item['category'].lower() or\n                search_term == str(item['id'])):\n                filtered_data.append(item)\n        \n        # Add filtered data to treeview\n        for item in filtered_data:\n            self.tree.insert('', tk.END, values=(\n                item['id'], item['name'], item['category'], \n                f\"${item['price']:.2f}\", item['quantity']\n            ))\n        \n        # Update status\n        total_items = len(filtered_data)\n        self.status_bar.set_status(f\"Showing {total_items} items\")\n    \n    def filter_data(self, *args):\n        \"\"\"Filter data based on search term\"\"\"\n        self.refresh_view()\n    \n    def sort_by_column(self, column):\n        \"\"\"Sort treeview by column\"\"\"\n        # Get all items\n        items = [(self.tree.set(item, column), item) for item in self.tree.get_children()]\n        \n        # Sort items\n        try:\n            # Try numeric sort\n            items.sort(key=lambda x: float(x[0].replace('$', '')))\n        except ValueError:\n            # Fallback to string sort\n            items.sort()\n        \n        # Reorder items in treeview\n        for index, (val, item) in enumerate(items):\n            self.tree.move(item, '', index)\n    \n    def add_item(self):\n        \"\"\"Add new item using dialog\"\"\"\n        dialog = ItemDialog(self.root, \"Add Item\")\n        if dialog.result:\n            new_id = max([item['id'] for item in self.data], default=0) + 1\n            new_item = {\n                'id': new_id,\n                'name': dialog.result['name'],\n                'category': dialog.result['category'],\n                'price': dialog.result['price'],\n                'quantity': dialog.result['quantity']\n            }\n            self.data.append(new_item)\n            self.refresh_view()\n            self.status_bar.set_status(f\"Added item: {new_item['name']}\")\n    \n    def edit_item(self):\n        \"\"\"Edit selected item\"\"\"\n        selection = self.tree.selection()\n        if not selection:\n            messagebox.showwarning(\"Warning\", \"Please select an item to edit.\")\n            return\n        \n        # Get selected item data\n        item_values = self.tree.item(selection[0])['values']\n        item_id = int(item_values[0])\n        \n        # Find item in data\n        item_data = next((item for item in self.data if item['id'] == item_id), None)\n        if not item_data:\n            return\n        \n        # Open edit dialog\n        dialog = ItemDialog(self.root, \"Edit Item\", item_data)\n        if dialog.result:\n            item_data.update(dialog.result)\n            self.refresh_view()\n            self.status_bar.set_status(f\"Updated item: {item_data['name']}\")\n    \n    def delete_item(self):\n        \"\"\"Delete selected item\"\"\"\n        selection = self.tree.selection()\n        if not selection:\n            messagebox.showwarning(\"Warning\", \"Please select an item to delete.\")\n            return\n        \n        if messagebox.askyesno(\"Confirm\", \"Are you sure you want to delete this item?\"):\n            # Get selected item ID\n            item_values = self.tree.item(selection[0])['values']\n            item_id = int(item_values[0])\n            \n            # Remove from data\n            self.data = [item for item in self.data if item['id'] != item_id]\n            self.refresh_view()\n            self.status_bar.set_status(\"Item deleted\")\n    \n    def new_file(self):\n        \"\"\"Create new file\"\"\"\n        if messagebox.askyesno(\"New File\", \"This will clear all data. Continue?\"):\n            self.data = []\n            self.refresh_view()\n            self.status_bar.set_status(\"New file created\")\n    \n    def open_file(self):\n        \"\"\"Open file dialog and load data\"\"\"\n        filename = filedialog.askopenfilename(\n            title=\"Open Data File\",\n            filetypes=[(\"JSON files\", \"*.json\"), (\"All files\", \"*.*\")]\n        )\n        \n        if filename:\n            try:\n                with open(filename, 'r') as f:\n                    self.data = json.load(f)\n                self.refresh_view()\n                self.status_bar.set_status(f\"Loaded {len(self.data)} items from {filename}\")\n            except Exception as e:\n                messagebox.showerror(\"Error\", f\"Failed to load file: {e}\")\n    \n    def save_file(self):\n        \"\"\"Save file dialog and save data\"\"\"\n        filename = filedialog.asksaveasfilename(\n            title=\"Save Data File\",\n            defaultextension=\".json\",\n            filetypes=[(\"JSON files\", \"*.json\"), (\"All files\", \"*.*\")]\n        )\n        \n        if filename:\n            try:\n                with open(filename, 'w') as f:\n                    json.dump(self.data, f, indent=2)\n                self.status_bar.set_status(f\"Saved {len(self.data)} items to {filename}\")\n            except Exception as e:\n                messagebox.showerror(\"Error\", f\"Failed to save file: {e}\")\n\n\n# 4. Dialog Example\nclass ItemDialog:\n    \"\"\"Custom dialog for adding/editing items\"\"\"\n    \n    def __init__(self, parent, title, item_data=None):\n        self.result = None\n        \n        # Create dialog window\n        self.dialog = tk.Toplevel(parent)\n        self.dialog.title(title)\n        self.dialog.geometry(\"300x200\")\n        self.dialog.transient(parent)\n        self.dialog.grab_set()\n        \n        # Center dialog\n        self.dialog.update_idletasks()\n        x = parent.winfo_x() + (parent.winfo_width() // 2) - 150\n        y = parent.winfo_y() + (parent.winfo_height() // 2) - 100\n        self.dialog.geometry(f\"300x200+{x}+{y}\")\n        \n        self.create_widgets(item_data)\n        \n        # Wait for dialog to close\n        self.dialog.wait_window()\n    \n    def create_widgets(self, item_data):\n        \"\"\"Create dialog widgets\"\"\"\n        main_frame = ttk.Frame(self.dialog, padding=\"10\")\n        main_frame.pack(fill=tk.BOTH, expand=True)\n        \n        # Form fields\n        self.name_field = LabeledEntry(main_frame, \"Name:\", entry_width=25)\n        self.category_field = LabeledEntry(main_frame, \"Category:\", entry_width=25)\n        self.price_field = LabeledEntry(main_frame, \"Price:\", entry_width=25)\n        self.quantity_field = LabeledEntry(main_frame, \"Quantity:\", entry_width=25)\n        \n        # Arrange fields\n        self.name_field.pack(fill=tk.X, pady=2)\n        self.category_field.pack(fill=tk.X, pady=2)\n        self.price_field.pack(fill=tk.X, pady=2)\n        self.quantity_field.pack(fill=tk.X, pady=2)\n        \n        # Populate fields if editing\n        if item_data:\n            self.name_field.set(item_data['name'])\n            self.category_field.set(item_data['category'])\n            self.price_field.set(str(item_data['price']))\n            self.quantity_field.set(str(item_data['quantity']))\n        \n        # Buttons\n        button_frame = ttk.Frame(main_frame)\n        button_frame.pack(fill=tk.X, pady=(10, 0))\n        \n        ok_button = ttk.Button(button_frame, text=\"OK\", command=self.ok_clicked)\n        cancel_button = ttk.Button(button_frame, text=\"Cancel\", command=self.cancel_clicked)\n        \n        ok_button.pack(side=tk.RIGHT, padx=(5, 0))\n        cancel_button.pack(side=tk.RIGHT)\n        \n        # Bind Enter and Escape\n        self.dialog.bind('<Return>', lambda e: self.ok_clicked())\n        self.dialog.bind('<Escape>', lambda e: self.cancel_clicked())\n        \n        # Focus on first field\n        self.name_field.focus()\n    \n    def ok_clicked(self):\n        \"\"\"Handle OK button click\"\"\"\n        try:\n            # Validate input\n            name = self.name_field.get().strip()\n            category = self.category_field.get().strip()\n            price = float(self.price_field.get())\n            quantity = int(self.quantity_field.get())\n            \n            if not name or not category:\n                messagebox.showerror(\"Error\", \"Name and category are required.\")\n                return\n            \n            if price < 0 or quantity < 0:\n                messagebox.showerror(\"Error\", \"Price and quantity must be non-negative.\")\n                return\n            \n            # Set result and close\n            self.result = {\n                'name': name,\n                'category': category,\n                'price': price,\n                'quantity': quantity\n            }\n            self.dialog.destroy()\n            \n        except ValueError:\n            messagebox.showerror(\"Error\", \"Please enter valid numeric values for price and quantity.\")\n    \n    def cancel_clicked(self):\n        \"\"\"Handle Cancel button click\"\"\"\n        self.dialog.destroy()\n\n\n# 5. Canvas Example with Drawing\nclass DrawingApp:\n    \"\"\"Simple drawing application using Canvas\"\"\"\n    \n    def __init__(self, root):\n        self.root = root\n        self.root.title(\"Drawing Application\")\n        self.root.geometry(\"600x500\")\n        \n        self.current_tool = \"pen\"\n        self.current_color = \"black\"\n        self.pen_size = 2\n        \n        self.create_widgets()\n        self.bind_events()\n    \n    def create_widgets(self):\n        \"\"\"Create drawing application widgets\"\"\"\n        # Toolbar\n        toolbar = ttk.Frame(self.root)\n        toolbar.pack(fill=tk.X, padx=5, pady=5)\n        \n        # Tool buttons\n        ttk.Button(toolbar, text=\"Pen\", command=lambda: self.set_tool(\"pen\")).pack(side=tk.LEFT, padx=2)\n        ttk.Button(toolbar, text=\"Brush\", command=lambda: self.set_tool(\"brush\")).pack(side=tk.LEFT, padx=2)\n        ttk.Button(toolbar, text=\"Eraser\", command=lambda: self.set_tool(\"eraser\")).pack(side=tk.LEFT, padx=2)\n        \n        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, padx=5, fill=tk.Y)\n        \n        # Color buttons\n        colors = [\"black\", \"red\", \"green\", \"blue\", \"yellow\", \"purple\"]\n        for color in colors:\n            btn = tk.Button(toolbar, bg=color, width=2, \n                          command=lambda c=color: self.set_color(c))\n            btn.pack(side=tk.LEFT, padx=1)\n        \n        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, padx=5, fill=tk.Y)\n        \n        # Size control\n        ttk.Label(toolbar, text=\"Size:\").pack(side=tk.LEFT, padx=(5, 2))\n        self.size_var = tk.IntVar(value=self.pen_size)\n        size_scale = ttk.Scale(toolbar, from_=1, to=20, orient=tk.HORIZONTAL, \n                              variable=self.size_var, command=self.update_size)\n        size_scale.pack(side=tk.LEFT, padx=2)\n        \n        ttk.Button(toolbar, text=\"Clear\", command=self.clear_canvas).pack(side=tk.RIGHT, padx=5)\n        \n        # Canvas\n        self.canvas = tk.Canvas(self.root, bg=\"white\", cursor=\"crosshair\")\n        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)\n        \n        # Drawing state\n        self.last_x = None\n        self.last_y = None\n    \n    def bind_events(self):\n        \"\"\"Bind canvas events\"\"\"\n        self.canvas.bind(\"<Button-1>\", self.start_draw)\n        self.canvas.bind(\"<B1-Motion>\", self.draw)\n        self.canvas.bind(\"<ButtonRelease-1>\", self.stop_draw)\n    \n    def set_tool(self, tool):\n        \"\"\"Set current drawing tool\"\"\"\n        self.current_tool = tool\n        if tool == \"eraser\":\n            self.canvas.config(cursor=\"dotbox\")\n        else:\n            self.canvas.config(cursor=\"crosshair\")\n    \n    def set_color(self, color):\n        \"\"\"Set current drawing color\"\"\"\n        self.current_color = color\n    \n    def update_size(self, value):\n        \"\"\"Update pen size\"\"\"\n        self.pen_size = int(float(value))\n    \n    def start_draw(self, event):\n        \"\"\"Start drawing\"\"\"\n        self.last_x = event.x\n        self.last_y = event.y\n    \n    def draw(self, event):\n        \"\"\"Draw on canvas\"\"\"\n        if self.last_x and self.last_y:\n            color = \"white\" if self.current_tool == \"eraser\" else self.current_color\n            width = self.pen_size * 3 if self.current_tool == \"brush\" else self.pen_size\n            \n            self.canvas.create_line(\n                self.last_x, self.last_y, event.x, event.y,\n                width=width, fill=color, capstyle=tk.ROUND, smooth=tk.TRUE\n            )\n        \n        self.last_x = event.x\n        self.last_y = event.y\n    \n    def stop_draw(self, event):\n        \"\"\"Stop drawing\"\"\"\n        self.last_x = None\n        self.last_y = None\n    \n    def clear_canvas(self):\n        \"\"\"Clear the canvas\"\"\"\n        self.canvas.delete(\"all\")\n\n\n# Demo function\ndef run_examples():\n    \"\"\"Run GUI programming examples\"\"\"\n    print(\"Choose an example to run:\")\n    print(\"1. Basic Application\")\n    print(\"2. Data Manager (Advanced)\")\n    print(\"3. Drawing Application\")\n    \n    choice = input(\"Enter choice (1-3): \").strip()\n    \n    root = tk.Tk()\n    \n    if choice == \"1\":\n        app = BasicApplication(root)\n    elif choice == \"2\":\n        app = DataManagerApp(root)\n    elif choice == \"3\":\n        app = DrawingApp(root)\n    else:\n        print(\"Invalid choice. Running basic application.\")\n        app = BasicApplication(root)\n    \n    root.mainloop()\n\n\nif __name__ == \"__main__\":\n    run_examples()")
