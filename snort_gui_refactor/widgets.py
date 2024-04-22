import tkinter as tk
from tkinter import ttk
from decimal import Decimal, InvalidOperation

class ValidatedMixin:
    """Adds validation functionality to an input widget"""

    def __init__(self, *args, error_var=None, **kwargs):
        self.error = error_var or tk.StringVar()
        super().__init__(*args, **kwargs)

        vcmd = self.register(self._validate)
        invcmd = self.register(self._invalid)

        self.configure(
            validate='all',
            validatecommand=(vcmd, '%P', '%s', '%S', '%V', '%i', '%d'),
            invalidcommand=(invcmd, '%P', '%s', '%S', '%V', '%i', '%d')
        )

    def _toggle_error(self, on=False):
        self.configure(foreground=('red' if on else 'black'))

    def _validate(self, proposed, current, char, event, index, action):
        self.error.set('')
        self._toggle_error()
        valid = True

        # if the widget is disabled, don't validate
        state = str(self.configure('state')[-1])
        if state == tk.DISABLED:
            return valid
        
        if event == 'focusout':
            valid = self._focusout_validate(event=event)
        elif event == 'key':
            valid = self._key_validate(
                proposed=proposed,
                current=current,
                char=char,
                event=event,
                index=index,
                action=action
            )
        return valid
    
    def _focusout_validate(self, **kwargs):
        return True
    
    def _key_validate(self, **kwargs):
        return True
    
    def _invalid(self, proposed, current, char, event, index, action):
        if event == 'focusout':
            self._focusout_invalid(event=event)
        elif event == 'key':
            self._key_invalid(
                proposed=proposed,
                current=current,
                char=char,
                event=event,
                index=index,
                action=action
            )

    def _focusout_invalid(self, **kwargs):
        """Handle invalid data on a focus event"""
        self._toggle_error(True)

    def _key_invalid(self, **kwargs):
        """Handle invalid data on a key event.
        By default do nothing"""
        pass

    def trigger_focusout_validation(self):
        valid = self._validate('', '', '', 'focusout', '', '')
        if not valid:
            self._focusout_invalid(event='focusout')
        return valid
    
class RequiredEntry(ValidatedMixin, ttk.Entry):
    """Entry that requires input"""

    def _focusout_validate(self, event):
        valid = True
        if not self.get():
            valid = False
            self.error.set('A value is required')
        return valid

class ValidatedCombobox(ValidatedMixin, ttk.Combobox):
    """A Combobox widget that only takes values from its string list"""

    def __init__(self, *args, focus_update_var=None, twin_var=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        if twin_var:
            self.twin_var = twin_var
            self.twin_var.trace_add('write', self._remove_value)
        
        self.focus_update_var = focus_update_var
        self.bind('<FocusOut>', self._set_focus_update_var)

    def _set_focus_update_var(self, event):
        value = self.get()
        if self.focus_update_var and not self.error.get():
            self.focus_update_var.set(value)

    def _remove_value(self, *_):
        self.set('')
        self.trigger_focusout_validation()

    def _key_validate(self, proposed, action, **kwargs):
        valid = True
        # Deletion is always valid
        if action == '0':
            self.set('')
            return True
        
        values = self.cget('values')
        # Do a case-insensitive match against entered text
        matching = [
            x for x in values
            if x.lower().startswith(proposed.lower())
        ]
        if len(matching) == 0:
            valid = False
        elif len(matching) == 1:
            self.set(matching[0])
            self.icursor(tk.END)
            valid = False
        return valid
    
    def _focusout_validate(self, **kwargs):
        valid = True
        if not self.get():
            valid = False
            self.error.set('A value is required')
        return valid
    
class ValidatedSpinbox(ValidatedMixin, ttk.Spinbox):
    """Spinbox widget that is range-limited"""

    def __init__(self, *args, from_='-Infinity', to='Infinity', **kwargs):
        super().__init__(*args, from_=from_, to=to, **kwargs)
        increment = Decimal(str(kwargs.get('increment', '1.0')))
        self.precision = increment.normalize().as_tuple().exponent

    def _key_validate(self, char, index, current, proposed, action, **kwargs):
        # Deletion is always valid
        if action == '0':
            return True
        valid = True
        min_val = self.cget('from')
        max_val = self.cget('to')
        no_negative = min_val >= 0
        no_decimal = self.precision >= 0

        if any([
            (char not in '-1234567890.'), # only valid chars
            (char == '-' and (no_negative or index != '0')), # '-' can only be in index 0, and only if negatives are allowed
            (char == '.' and (no_decimal or '.' in current)) # '.'only allowed if precision < 1, and is only allowed once
        ]):
            return False
        
        if proposed in '-.':
            return True
        
        proposed = Decimal(proposed)
        proposed_precision = proposed.as_tuple().exponent

        if any([
            (proposed > max_val), # proposed cannot be > max
            (proposed_precision < self.precision) # proposed cannot be more precise than increment precision
        ]):
            return False
        
        return valid
    
    def _focusout_validate(self, **kwargs):
        valid = True
        value = self.get()
        min_val = self.cget('from')
        max_val = self.cget('to')

        try:
            d_value = Decimal(value)
        except InvalidOperation:
            self.error.set(f'Invalid number string: {value}')
            return False
        
        if d_value < min_val:
            self.error.set(f'Value is too low (min {min_val})')
            valid = False
        if d_value > max_val:
            self.error.set(f'Value is too high )max {max_val}')
            valid = False
        return valid

class LabelInput(tk.Frame):
    """A label and input widget combined"""

    def __init__(
            self, parent, label, var, input_class=ttk.Entry,
            input_args=None, label_args=None, position="top", 
            disable_var=None, *args, **kwargs
    ):
        super().__init__(parent, *args, **kwargs)

        input_args = input_args or {}
        label_args = label_args or {}
        self.variable = var
        self.variable.label_widget = self


        if input_class in (ttk.Checkbutton, ttk.Button):
            input_args["text"] = label
        else:
            self.label = ttk.Label(self, text=label, **label_args)
            self.label.grid(row=0, column=0, sticky=(tk.E + tk.W))

        if input_class in (ttk.Checkbutton, ttk.Button, ttk.Radiobutton, ttk.OptionMenu):
            input_args["variable"] = self.variable
        else:
            input_args["textvariable"] = self.variable

        if input_class == ttk.Radiobutton:
            self.input = tk.Frame(self)
            for v in input_args.pop('values', []):
                button = ttk.Radiobutton(self, value=v, text=v, **input_args)
                button.pack(side=tk.LEFT, ipadx=10, ipady=2, expand=True, fill='x')
        if input_class == ttk.OptionMenu:
            self.input = ttk.OptionMenu(self, self.variable, *input_args['values'])
        else:
            self.input = input_class(self, **input_args)

        if position == "top":
            self.input.grid(row=1, column=0, sticky=(tk.E + tk.W))
            self.columnconfigure(0, weight=1)
        else:
            self.input.grid(row=0, column=1, sticky=(tk.E + tk.W))
            self.columnconfigure(1, weight=1)

        if disable_var:
            self.disable_var = disable_var
            self.disable_var.trace_add('write', self._check_disable)

    def _check_disable(self, *_):
        if not hasattr(self, 'disable_var'):
            return
        
        if self.disable_var.get():
            self.input.configure(state=tk.DISABLED)
            self.variable.set('')
        else:
            self.input.configure(state=tk.NORMAL)

    def grid(self, sticky=(tk.E + tk.W), **kwargs):
        """Override grid to add sticky by default"""
        super().grid(sticky=sticky, **kwargs)

class BoundText(tk.Text):
    """A Text widget with a bound variable."""
    
    def __init__(self, *args, textvariable=None, **kwargs):
        super().__init__(*args, **kwargs)

        # Bound variable
        self._variable = textvariable

        # Insert contents info widget
        # We normally want the text box to be disabled so that the user can't type into it
        # So when inserting text, we first need to enable the widget, then re-disable it after
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
