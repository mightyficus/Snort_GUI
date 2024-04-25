"""
Copyright 2024 Cooper Hopkin
    This file is part of Snort Rule Builder.
    Snort Rule Builder is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
    Snort Rule Builder is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along with Snort Gui. If not, see <https://www.gnu.org/licenses/>. 
"""

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

    def _update_rule(self, *_):
        rule_header = f"{self._vars['Action'].get()} {self._vars['Protocol'].get()} {self._vars['Source IP'].get()} {self._vars['Source Port'].get()} {self._vars['Direction'].get()} {self._vars['Destination IP'].get()} {self._vars['Destination Port'].get()}"
        rule_body = ' ('
        # print(self._vars['Message'].get())
        if len(self._vars['Message'].get()) != 0:
            rule_body = rule_body + f"\n\tmsg:\"{self._vars['Message'].get()}\";"
        # Protocol specific options
        if self._vars['Protocol'].get() == 'tcp':
            self._vars['tcp_disabled'].set(False)
            self._vars['flow_disabled'].set(False)
            self._vars['udp_disabled'].set(True)
            self._vars['icmp_disabled'].set(True)
            if len(self._vars['Request Method'].get()) != 0:
                rule_body = rule_body + f"\n\thttp_method;\n\tcontent:\"{self._vars['Request Method'].get()}\"; /* Request Method */"
            if len(self._vars['Response Code'].get()) != 0:
                # print(f'{len(self._vars["Response Code"].get())}: {self._vars["Response Code"].get()}')
                rule_body = rule_body + f"\n\thttp_stat_code;\n\tcontent:\"{self._vars['Message'].get()}\";/* Response Code */"
            if len(self._vars['Flow'].get()) != 0:
                rule_body = rule_body + f"\n\tflow:\"{self._vars['Flow'].get()}\";"

        elif self._vars['Protocol'].get() == 'udp':
            self._vars['tcp_disabled'].set(True)
            self._vars['flow_disabled'].set(False)
            self._vars['udp_disabled'].set(False)
            self._vars['icmp_disabled'].set(True)
            if len(self._vars['Flow'].get()) != 0:
                rule_body = rule_body + f"\n\tflow:\"{self._vars['Flow'].get()}\";"

        elif self._vars['Protocol'].get() == 'icmp':
            self._vars['tcp_disabled'].set(True)
            self._vars['flow_disabled'].set(True)
            self._vars['udp_disabled'].set(True)
            self._vars['icmp_disabled'].set(False)
            if len(self._vars['ICMP Type'].get()) != 0:
                rule_body = rule_body + f"\n\titype:{self._vars['ICMP Type'].get()};"
            if len(self._vars['ICMP Code'].get()) != 0:
                rule_body = rule_body + f"\n\ticode:{self._vars['ICMP Code'].get()};"



        if len(self._vars['Class Type'].get()) != 0:
            rule_body = rule_body + f"\n\tclasstype:{self._vars['Class Type'].get()};"
        if self._vars['Priority'] != '':
            rule_body = rule_body + f"\n\tpriority:{self._vars['Priority'].get()};"
        if self._vars['SID'] != '':
            rule_body = rule_body + f"\n\tsid:{self._vars['SID'].get()};"
        if self._vars['Revision Number'] != '':
            rule_body = rule_body + f"\n\trev:{self._vars['Revision Number'].get()};\n)"

        rule_body = rule_body

        self._vars['Rule'].set(rule_header + rule_body)


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
            'Request Method': tk.StringVar(value=""),
            'Response Code': tk.StringVar(value=""),
            'Flow': tk.StringVar(),
            #'Flags': [],
            'ICMP Type': tk.StringVar(),
            'ICMP Code': tk.StringVar(),
            'port_disabled': tk.BooleanVar(value=False),
            'tcp_disabled': tk.BooleanVar(value=False),
            'udp_disabled': tk.BooleanVar(value=True),
            'flow_disabled': tk.BooleanVar(value=False),
            'icmp_disabled': tk.BooleanVar(value=True)
        }
        self._vars['Protocol'].trace_add('write', self._prot_callback)

        # TODO: Add a trace with a callback that modifies the rule variable

        ##################################### Important Info ##############################
        m_info = self._add_frame("Main Information", cols=9)

        w.LabelInput(
            m_info, "Action",
            input_class=ttk.OptionMenu,
            var=self._vars['Action'],
            input_args={'values': c.actions}
        ).grid(row=0, column=0)

        w.LabelInput(
            m_info, "Protocol",
            input_class=ttk.OptionMenu,
            var=self._vars['Protocol'],
            input_args={'values': c.protocols}
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
            input_args={'values': ['->', '<>']}
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
            input_args={'from_': 1, 'to': 2147483647, 'increment': 1}
        ).grid(row=1, column=8)

        ################################# Body Options ####################################
        b_info = self._add_frame("Body Options", cols=1)

        w.LabelInput(
            b_info, "Request Method",
            input_class=w.ValidatedCombobox,
            var=self._vars['Request Method'],
            disable_var=self._vars['tcp_disabled'],
            input_args={'values': c.http_request_methods, 'twin_var': self._vars['Response Code']}
        ).grid(row=0, column=0)

        w.LabelInput(
            b_info, "Response Code",
            input_class=w.ValidatedCombobox,
            var=self._vars['Response Code'],
            disable_var=self._vars['tcp_disabled'],
            input_args={'values': c.http_codes, 'twin_var': self._vars['Request Method']}
        ).grid(row=1, column=0)

        w.LabelInput(
            b_info, "Flow",
            input_class=w.ValidatedCombobox,
            var=self._vars['Flow'],
            disable_var=self._vars['flow_disabled'],
            input_args={'values': c.flow}
        ).grid(row=2, column=0)

        w.LabelInput(
            b_info, "ICMP Type",
            input_class=w.ValidatedCombobox,
            var=self._vars['ICMP Type'],
            disable_var=self._vars['icmp_disabled'],
            input_args={'values': c.icmp_types}
        ).grid(row=3, column=0)

        w.LabelInput(
            b_info, "ICMP Code",
            input_class=w.ValidatedCombobox,
            var=self._vars['ICMP Code'],
            disable_var=self._vars['icmp_disabled'],
            input_args={'values': [str(x) for x in range(17)]}
        ).grid(row=4, column=0)
        self._update_rule()
        for key, value in self._vars.items():
            if key != 'Rule':
                self._vars[key].trace_add('write', self._update_rule)

        ################################# Rule Output #####################################

        w.LabelInput(
            self, "Rule",
            input_class=w.BoundText,
            var=self._vars['Rule'],
            input_args={'width': 75, 'height':10}
        ).grid(row=3, column=0, sticky=(tk.W + tk.E))