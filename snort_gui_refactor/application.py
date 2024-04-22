import tkinter as tk
from tkinter import ttk
from . import views as v

class Application(tk.Tk):
    """Application root window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Snort Rule Builder")
        self.columnconfigure(0, weight=1)

        ttk.Label(
            self,
            text="Snort Rule Builder",
            font=("TkDefaultFont", 16),
        ).grid(row=0)

        self.SnortRuleHeaderForm = v.SnortRuleHeaderForm(self)
        self.SnortRuleHeaderForm.grid(row=1, padx = 10, sticky=(tk.W + tk.E))