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
        
class BoundText(tk.Text):
  """A Text widget with a bound variable."""

  def __init__(self, *args, textvariable=None, **kwargs):
    super().__init__(*args, **kwargs)
    self._variable = textvariable
    if self._variable:
        self.config(state=tk.NORMAL)
        # insert any default value
        self.insert('1.0', self._variable.get())
        self._variable.trace_add('write', self._set_content)
        self.bind('<<Modified>>', self._set_var)
    self.config(state=tk.DISABLED)

  def _set_var(self, *_):
    """Set the variable to the text contents"""
    if self.edit_modified():
      content = self.get('1.0', 'end-1chars')
      self._variable.set(content)
      self.edit_modified(False)

  def _set_content(self, *_):
    """Set the text contents to the variable"""
    self.config(state=tk.NORMAL)
    self.delete('1.0', tk.END)
    self.insert('1.0', self._variable.get())
    self.config(state=tk.DISABLED)