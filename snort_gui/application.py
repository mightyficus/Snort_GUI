"""
Copyright 2024 Cooper Hopkin
    This file is part of Snort Rule Builder.
    Snort Rule Builder is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
    Snort Rule Builder is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along with Snort Rule Builder. If not, see <https://www.gnu.org/licenses/>. 
"""

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
