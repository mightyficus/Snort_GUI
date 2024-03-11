import tkinter as tk
from tkinter import ttk

class SnortRuleForm(ttk.Frame):
    """View for inputting options for Snort Rules"""
    
    def _add_frame(self, label, cols=3):
        """Add a LabelFrame to the form"""
        
        frame = ttk.LabelFrame(self, text=label)
        frame.grid(sticky=tk.W + tk.E)
        for i in range(cols):
            frame.columnconfigure(i, weight=1)
        return frame
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)