import tkinter as tk
from tkinter import ttk

from . import widgets as w
from .constants import menus as c

class SnortRuleHeaderForm(ttk.Frame):
    """Input frame for widgets"""

    def _add_frame(self, label, cols=3):
        """Add a LabelFrame to the form"""

        frame = ttk.LabelFrame(self, text=label)
        frame.grid(sticky=(tk.E + tk.W))
        for i in range(cols):
            frame.columnconfigure(i, weight=1)
        return frame
    
    def _prot_callback(self, *_):
        if self._vars['Protocol'].get() == 'icmp':
            self._vars['port_disabled'].set(True)
        else:
            self._vars['port_disabled'].set(False)
            self._vars['Source Port'].set('any')
            self._vars['Destination Port'].set('any')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._vars = {
            'Action': tk.StringVar(),
            'Protocol': tk.StringVar(),
            'Source IP': tk.StringVar(value='any'),
            'Source Port': tk.StringVar(value='any'),
            'Direction': tk.StringVar(),
            'Destination IP': tk.StringVar(value='any'),
            'Destination Port': tk.StringVar(value='any'),
            'SID': tk.IntVar(value=1000001),
            'Revision Number': tk.IntVar(value=1),
            'Class Type': tk.StringVar(),
            'Priority': tk.IntVar(value=5),
            'Message': tk.StringVar(),
            'Rule': tk.StringVar(),
            'port_disabled': tk.BooleanVar(value=False)
        }
        self._vars['Protocol'].trace_add('write', self._prot_callback)

        # TODO: Add a trace with a callback that modifies the rule variable

        ##################################### Important Info ##############################
        m_info = self._add_frame("Main Information", cols=9)

        w.LabelInput(
            m_info, "Action",
            input_class=ttk.OptionMenu,
            var=self._vars['Action'],
            input_args={'default': 'alert', 'values': c.actions}
        ).grid(row=0, column=0)

        w.LabelInput(
            m_info, "Protocol",
            input_class=ttk.OptionMenu,
            var=self._vars['Protocol'],
            input_args={'default': 'tcp', 'values': c.protocols}
        ).grid(row=0, column=1)

        w.LabelInput(
            m_info, "Source IP",
            input_class=w.RequiredEntry,
            var=self._vars['Source IP']
        ).grid(row=0, column=2)

        w.LabelInput(
            m_info, "Source Port",
            var=self._vars['Source Port'],
            disable_var=self._vars['port_disabled']
        ).grid(row=0, column=3)

        w.LabelInput(
            m_info, "Direction",
            input_class=ttk.OptionMenu,
            var=self._vars['Direction'],
            input_args={'default': '->', 'values': ['->', '->', '<>']}
        ).grid(row=0, column=4)

        w.LabelInput(
            m_info, "Destination IP",
            input_class=w.RequiredEntry,
            var=self._vars['Destination IP']
        ).grid(row=0, column=5)

        w.LabelInput(
            m_info, "Destination Port",
            var=self._vars['Destination Port'],
            disable_var=self._vars['port_disabled']
        ).grid(row=0, column=6)

        w.LabelInput(
            m_info, "SID",
            input_class=w.ValidatedSpinbox,
            var=self._vars['SID'],
            input_args={'from_': 1000001, 'increment': 1}
        ).grid(row=0, column=7)
        
        w.LabelInput(
            m_info, "Revision Number",
            input_class=w.ValidatedSpinbox,
            var=self._vars['Revision Number'],
            input_args={'from_': 1, 'increment': 1}
        ).grid(row=0, column=8)

        w.LabelInput(
            m_info, "Message",
            var=self._vars['Message']
        ).grid(row=1, column=0, columnspan=7)

        w.LabelInput(
            m_info, "Class Type",
            input_class=w.ValidatedCombobox,
            var=self._vars['Class Type'],
            input_args={'values': c.class_types}
        ).grid(row=1, column=7)

        w.LabelInput(
            m_info, "Priority",
            input_class=w.ValidatedSpinbox,
            var=self._vars['Priority'],
            input_args={'from_': 1, 'to': 5, 'increment': 1}
        ).grid(row=1, column=8)

        ################################# Rule Output #####################################

        w.LabelInput(
            self, "Rule",
            input_class=w.BoundText,
            var=self._vars['Rule'],
            input_args={'width': 75, 'height':10}
        ).grid(row=3, column=0, sticky=(tk.W + tk.E))