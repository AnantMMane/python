import os
import time
import inspect
import importlib
import json
import cProfile
import ollama
import re
from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax

console = Console()

def ask_ai_pretty(prompt, model="codellama:7b"):
    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )['message']['content'].strip()
    except Exception as e:
        console.print(f"[bold red]❌ Error from model: {e}[/bold red]")
        return

    # 🔍 Check for code blocks with ``` markers
    if "```" in response:
        blocks = re.findall(r"```(\w+)?\n(.*?)```", response, re.DOTALL)
        if blocks:
            for lang, code in blocks:
                lang = lang.strip() if lang else "python"
                syntax = Syntax(code, lang, line_numbers=True, theme="monokai")
                console.print(syntax)
        else:
            # fallback to markdown if regex fails
            console.print(Markdown(response))
    else:
        console.print(Markdown(response))

# Optional: Data/Plotting/AI
try:
    import pandas as pd
except ImportError:
    pd = None

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

try:
    import openai
except ImportError:
    openai = None

from ptpython.layout import CompletionVisualisation
from pygments.styles.dracula import DraculaStyle  # Theme: 'dracula'

# ─────────────────────────────────────────────
# 🔧 Utility Functions
# ─────────────────────────────────────────────

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def timer(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    print(f"⏱️ Execution time: {end - start:.6f} seconds")
    return result

def inspect_obj(obj):
    print("📌 Type:", type(obj))
    print("📚 Docstring:\n", inspect.getdoc(obj))
    print("🔧 Attributes/Methods:\n", dir(obj))

def reload_module(module):
    return importlib.reload(module)

def log(text, level="info"):
    levels = {
        "info": "[INFO]",
        "warn": "[WARN]",
        "error": "[ERROR]",
        "success": "[OK]",
    }
    prefix = levels.get(level.lower(), "[INFO]")
    print(f"{prefix} {text}")

def save_output(obj, file='output.json'):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=4, ensure_ascii=False)
    print(f"✅ Saved to {file}")

def load_csv_quick(path):
    if pd:
        df = pd.read_csv(path)
        print(f"📊 Loaded {len(df)} rows, {len(df.columns)} columns")
        return df
    else:
        print("❌ pandas not installed. Run: pip install pandas")

def plot_quick(x, y, label="Plot", xlabel="X", ylabel="Y"):
    if plt:
        plt.figure(figsize=(6, 4))
        plt.plot(x, y, label=label)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(label)
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("❌ matplotlib not installed. Run: pip install matplotlib")

def profile(func, *args, **kwargs):
    print(f"⏱️ Profiling {func.__name__}...")
    cProfile.runctx("func(*args, **kwargs)", globals(), locals())

def ask_ai(prompt, model="codellama:7b"):
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"⚠️ Error using {model}: {e}"

# ─────────────────────────────────────────────
# 🧠 ptpython REPL Configuration
# ─────────────────────────────────────────────

def configure(repl):
    # 🌈 Visual Appearance
    repl.use_code_colorscheme('dracula')  # Try: monokai, vim, pastie, native
    repl.show_status_bar = True
    repl.show_line_numbers = True
    repl.highlight_matching_parenthesis = True

    # ⚙️ Behavior
    repl.confirm_exit = False
    repl.enable_auto_suggest = True
    repl.enable_fuzzy_completion = True
    repl.enable_dictionary_completion = True
    repl.enable_open_in_editor = True  # Press F4 for multi-line editing
    repl.vi_mode = False
    repl.paste_mode = False
    repl.completion_visualisation = CompletionVisualisation.POP_UP
    repl.complete_while_typing = True
    repl.use_extra_opening_paren = True

    # 🧩 Preload helper functions
    repl.get_globals().update({
        'clear': clear,
        'timer': timer,
        'inspect_obj': inspect_obj,
        'reload_module': reload_module,
        'log': log,
        'save_output': save_output,
        'load_csv_quick': load_csv_quick,
        'plot_quick': plot_quick,
        'profile': profile,
        'ask_ai': ask_ai,
        'ask_ai_preety' : ask_ai_pretty,
    })
