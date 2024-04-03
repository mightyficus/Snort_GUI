import tkinter as tk
from tkinter import ttk
from . import widgets as w

class SnortRuleForm(ttk.Frame):
    """View for inputting options for Snort Rules"""
    
    def _add_frame(self, label, cols=3):
        """Add a LabelFrame to the form"""
        
        frame = ttk.LabelFrame(self, text=label)
        frame.grid(sticky=tk.W + tk.E)
        for i in range(cols):
            frame.columnconfigure(i, weight=1)
        return frame
    
    def _prot_change(self, *_):
        self.rule_box.config(state=tk.NORMAL)
            
        if self._vars["Protocol"].get() == 'tcp' or self._vars["Protocol"].get() == 'udp':
            self._vars["Rule"].set(f'{self._vars["Action"].get()} {self._vars["Protocol"].get()} {self._vars["Source IP"].get()} {self._vars["Source Port"].get()} {self._vars["Direction"].get()} {self._vars["Destination IP"].get()} {self._vars["Destination Port"].get()}\n(\n\tmsg:"{self._vars["Message"].get()}";\n\tclasstype:{self._vars["Class Type"].get()};\n\tpriority:{self._vars["Priority"].get()};\n\tsid:{self._vars["SID"].get()};\n\trev:{self._vars["Revision Number"].get()};\n)')
        elif self._vars["Protocol"].get() == "icmp":
            self._vars["Rule"].set(f'{self._vars["Action"].get()} {self._vars["Protocol"].get()} {self._vars["Source IP"].get()} {self._vars["Direction"].get()} {self._vars["Destination IP"].get()}\n(\n\tmsg:"{self._vars["Message"].get()}";\n\tclasstype:{self._vars["Class Type"].get()};\n\tpriority:{self._vars["Priority"].get()};\n\tsid:{self._vars["SID"].get()};\n\trev:{self._vars["Revision Number"].get()};\n)')
        else:
            self._vars["Rule"].set('any -> any ()')
            
        self.rule_box._set_content()
        
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self._vars = dict()
        
        #Build the form
        self.columnconfigure(0, weight=1)
        
        # Rule Header info
        h_info = self._add_frame("Header Info", cols=9)
        
        # Line 1
        # Action
        tk.Label(h_info, text="Action").grid(row=0, column=0, sticky=(tk.E + tk.W))
        action_options = [
            "alert",
            "block",
            "drop",
            "log",
            "pass"
        ]
        #rule_action = tk.StringVar()
        self._vars["Action"] = tk.StringVar()
        self._vars["Action"].set("alert")
        action_menu = ttk.OptionMenu(h_info, self._vars["Action"], "alert", *action_options)
        action_menu.grid(row=1, column=0, sticky=(tk.E + tk.W))
        
        # Protocol
        tk.Label(h_info, text="Protocol").grid(row=0, column=1, sticky=(tk.E + tk.W))
        protocol_options = [
            "tcp",
            "udp",
            "icmp"
        ]
        #rule_prot = tk.StringVar()
        self._vars["Protocol"] = tk.StringVar()
        self._vars["Protocol"].set("tcp")
        prot_menu = ttk.OptionMenu(h_info, self._vars["Protocol"], "tcp", *protocol_options)
        prot_menu.grid(row=1, column=1, sticky=(tk.E + tk.W))
        
        # Source IP
        tk.Label(h_info, text="Source IP").grid(row=0, column=2, sticky=(tk.E + tk.W))
        #rule_sip = tk.StringVar(value="Source IP")
        self._vars["Source IP"] = tk.StringVar()
        self._vars["Source IP"].set("any")
        sip_entry = ttk.Entry(h_info, textvariable=self._vars["Source IP"])
        sip_entry.grid(row=1, column=2, sticky=(tk.E + tk.W))
        
        # Source Port
        tk.Label(h_info, text="Source Port").grid(row=0, column=3, sticky=(tk.E + tk.W))
        #rule_sport = tk.StringVar(value="Source Port")
        self._vars["Source Port"] = tk.StringVar()
        self._vars["Source Port"].set("any")
        sport_entry = ttk.Entry(h_info, textvariable=self._vars["Source Port"])
        sport_entry.grid(row=1, column=3, sticky=(tk.E + tk.W))
        
        # Direction
        tk.Label(h_info, text="Direction").grid(row=0, column=4, sticky=(tk.E + tk.W))
        direction_options = [
            "->",
            "<>"
        ]
        #rule_dir = tk.StringVar()
        self._vars["Direction"] = tk.StringVar()
        self._vars["Direction"].set("->")
        dir_menu = ttk.OptionMenu(h_info, self._vars["Direction"], "->", *direction_options)
        dir_menu.grid(row=1, column=4, sticky=(tk.E + tk.W))
        
        # Destination IP
        tk.Label(h_info, text="Destination IP").grid(row=0, column=5, sticky=(tk.E + tk.W))
        #rule_dip = tk.StringVar(value="Dest IP")
        self._vars["Destination IP"] = tk.StringVar()
        self._vars["Destination IP"].set("any")
        dip_entry = ttk.Entry(h_info, textvariable=self._vars["Destination IP"])
        dip_entry.grid(row=1, column=5, sticky=(tk.E + tk.W))
        
        # Destination Port
        tk.Label(h_info, text="Destination Port").grid(row=0, column=6, sticky=(tk.E + tk.W))
        #rule_dport = tk.StringVar(value="Dest Port")
        self._vars["Destination Port"] = tk.StringVar()
        self._vars["Destination Port"].set("any")
        dport_entry = ttk.Entry(h_info, textvariable=self._vars["Destination Port"])
        dport_entry.grid(row=1, column=6, sticky=(tk.E + tk.W))
        
        # SID
        tk.Label(h_info, text="SID").grid(row=0, column=7, sticky=(tk.E + tk.W))
        #rule_sid = tk.StringVar(value="SID")
        self._vars["SID"] = tk.StringVar()
        sid_entry = ttk.Entry(h_info, textvariable=self._vars["SID"])
        sid_entry.grid(row=1, column=7, sticky=(tk.E + tk.W))
        
        # Revision Number
        tk.Label(h_info, text="Revision number").grid(row=0, column=8, sticky=(tk.E + tk.W))
        #rule_revnum = tk.StringVar(value="Rev Number")
        self._vars["Revision Number"] = tk.StringVar()
        revnum_entry = ttk.Entry(h_info, textvariable=self._vars["Revision Number"])
        revnum_entry.grid(row=1, column=8, sticky=(tk.E + tk.W))
        
        # Line 2
        # Message
        tk.Label(h_info, text="Message").grid(row=2, column=0, columnspan=7, sticky=(tk.W))
        #rule_message = tk.StringVar()
        self._vars["Message"] = tk.StringVar()
        message_entry = ttk.Entry(h_info, textvariable=self._vars["Message"])
        message_entry.grid(row=3, column=0, columnspan= 7, sticky=(tk.E + tk.W))
        
        # Class Type
        tk.Label(h_info, text="Class Type").grid(row=2, column=7, sticky=(tk.E + tk.W))
        #rule_classtype = tk.StringVar()
        self._vars["Class Type"] = tk.StringVar()
        classtype_entry = ttk.Entry(h_info, textvariable=self._vars["Class Type"])
        classtype_entry.grid(row=3, column=7, sticky=(tk.E + tk.W))
        
        # Priority
        tk.Label(h_info, text="Priority").grid(row=2, column=8, sticky=(tk.E + tk.W))
        priority_options = [
            "5",
            "4",
            "3",
            "2",
            "1"
        ]
        #rule_priority = tk.StringVar()
        self._vars["Priority"] = tk.StringVar()
        priority_menu = ttk.OptionMenu(h_info, self._vars["Priority"], "5", *priority_options)
        priority_menu.grid(row=3, column=8, sticky=(tk.E + tk.W))
        
        r_info = self._add_frame("Rule", cols=1)
        
        self._vars["Rule"] = tk.StringVar()
        self.rule_box = w.BoundText(r_info, textvariable=self._vars["Rule"])
        self.rule_box.grid(row=0, column=0, sticky=(tk.N + tk.S + tk.E + tk.W))
        
        for key, value in self._vars.items():
            value.trace("w", self._prot_change)
        self._prot_change()
        
        
        
        
        
        
        
        
        