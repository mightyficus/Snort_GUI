#snort_gui/widgets.py
"""Create custom Tkinter widgets using mixins
Widgets:
* IP Validated Entry
"""

import tkinter as tk
from tkinter import ttk

class ValidatedMixin:
    """Enable validation for input widgets"""
    
    def __init__(self, *args, error_var=None, **kwargs):
        self.error = error_var or tk.StringVar()
        super().__init__(*args, **kwargs)
        
        
