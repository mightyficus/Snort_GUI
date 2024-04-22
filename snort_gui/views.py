import tkinter as tk
from tkinter import ttk
from . import widgets as w
from .constants import Menus as m

class SnortRuleForm(ttk.Frame):
    """View for inputting options for Snort Rules"""
    
    def _add_frame(self, label, cols=3):
        """Add a LabelFrame to the form"""
        
        frame = ttk.LabelFrame(self, text=label)
        frame.grid(sticky=tk.W + tk.E)
        for i in range(cols):
            frame.columnconfigure(i, weight=1)
        return frame
    
    # def http_callback(self, varname, index, event):
    #     if varname == "HTTP Request":
    #         if self._body_vars["HTTP Request"].get() != "":
    #             self._body_vars["HTTP Response"].set("")
    #     if varname == "HTTP Response":
    #         if self._body_vars["HTTP Response"].get() != "":
    #             self._body_vars["HTTP Request"].set("")
    
    def _protocol_tcp(self, parent):
        # Set up header options: Action Protocol SrcIP SrcPort -> DestIP DestPort
        header_part = f'{self._vars["Action"].get()} {self._vars["Protocol"].get()} {self._vars["Source IP"].get()} {self._vars["Source Port"].get()} {self._vars["Direction"].get()} {self._vars["Destination IP"].get()} {self._vars["Destination Port"].get()}'
        # TODO: HTTP Request, HTTP Response, Flags, Flow

        body_part = "("
        if self._body_vars["Message"].get() != "":
            body_part = body_part + f'\n\tmsg:"{self._body_vars["Message"].get()}";'
        if self._body_vars["Class Type"].get() != "":
            body_part = body_part + f'\n\tclasstype:{self._body_vars["Class Type"].get()};'

        # HTTP Request Method
        tk.Label(parent, text="HTTP Request Method").grid(row=0, column=0, sticky=(tk.W))
        response_menu = ttk.OptionMenu(parent, self._body_vars["HTTP Request"], self._body_vars["HTTP Request"].get(), *m.http_request_methods)
        response_menu.grid(row=0, column=1, sticky=(tk.W + tk.E))
        
        # HTTP Response Code
        # Currently list of response codes is small, because a long list freaks out on small screens.
        # This could probably be fixed with an enhanced OptionMenu that has a scrollbar, but this will be 
        # fine for now.
        # Because of how the view refreshes, entry boxes don't work well.
        tk.Label(parent, text="HTTP Response Code").grid(row=1, column=0, sticky=(tk.W))
        response_menu = ttk.OptionMenu(parent, self._body_vars["HTTP Response"], self._body_vars["HTTP Response"].get(), *m.http_codes)
        #response_entry = ttk.Entry(parent, textvariable=self._body_vars["HTTP Response"])
        response_menu.grid(row=1, column=1, sticky=(tk.W + tk.E))

        if self._body_vars["HTTP Request"].get() != "":
            #self._body_vars["HTTP Response"].trace_remove("write", self._body_vars["HTTP Response"].trace_info()[0][1])
            #self._body_vars["HTTP Response"].set("")
            #self._body_vars["HTTP Response"].trace_add("write", self._prot_change)
            body_part = body_part + f'\n\thttp_method; content:"{self._body_vars["HTTP Request"].get()}";'
        if self._body_vars["HTTP Response"].get() != "":
            #self._body_vars["HTTP Request"].trace_remove("write", self._body_vars["HTTP Request"].trace_info()[0][1])
            #self._body_vars["HTTP Request"].set("")
            #self._body_vars["HTTP Request"].trace_add("write", self._prot_change)
            body_part = body_part + f'\n\thttp_stat_code; content:"{self._body_vars["HTTP Response"].get()}";'
            
        
        # HTTP Flags
        # Can't figure this out at the moment, mostly because because the logic to turn it in the 
        # rule is going to be funky
        # tk.Label(parent, text="Flags").grid(row=2, column=0, sticky=(tk.W))
        # tk.Label(parent, text="").grid(row=3, column=0, sticky=(tk.W))
        # flag_frame = tk.Frame(parent)
        # for col in range(3):
        #     flag_frame.columnconfigure(col, weight=1)
        
        
        
        #HTTP flow
        tk.Label(parent, text="Flow").grid(row=4, column=0, sticky=(tk.W))
        flow_menu = ttk.OptionMenu(parent, self._body_vars["TCP Flow"], self._body_vars["TCP Flow"].get(), *m.flow)
        flow_menu.grid(row=4, column=1, sticky=(tk.W + tk.E))
        if self._body_vars["TCP Flow"].get() != "":
            body_part = body_part + f'\n\tflow:"{self._body_vars["TCP Flow"].get()}";'

        if self._body_vars["Priority"].get() != "":
            body_part = body_part + f'\n\tpriority:{self._body_vars["Priority"].get()};'
        if self._body_vars["SID"].get() != "":
            body_part = body_part + f'\n\tsid:{self._body_vars["SID"].get()};'
        if self._body_vars["GID"].get() != "":
            body_part = body_part + f'\n\tgid:{self._body_vars["GID"].get()};'
        if self._body_vars["Revision Number"].get() != "":
            body_part = body_part + f'\n\trev:{self._body_vars["Revision Number"].get()};'

        body_part = body_part + "\n)"
        # Concatenate header and body
        self._vars["Rule"].set(f'{header_part}{body_part}')
        
    def _protocol_udp(self, parent):
        # Set up header options: Action Protocol SrcIP SrcPort -> DestIP DestPort
        header_part = f'{self._vars["Action"].get()} {self._vars["Protocol"].get()} {self._vars["Source IP"].get()} {self._vars["Source Port"].get()} {self._vars["Direction"].get()} {self._vars["Destination IP"].get()} {self._vars["Destination Port"].get()}'
        # TODO: Flow
        body_part = "("
        if self._body_vars["Message"].get() != "":
            body_part = body_part + f'\n\tmsg:"{self._body_vars["Message"].get()}";'
        if self._body_vars["Class Type"].get() != "":
            body_part = body_part + f'\n\tclasstype:{self._body_vars["Class Type"].get()};'
        
        #Traffic flow
        tk.Label(parent, text="").grid(row=0, column=0, sticky=(tk.W))
        tk.Label(parent, text="").grid(row=1, column=0, sticky=(tk.W))
        tk.Label(parent, text="Flow").grid(row=2, column=0, sticky=(tk.W))
        flow_menu = ttk.OptionMenu(parent, self._body_vars["UDP Flow"], self._body_vars["UDP Flow"].get(), *m.flow)
        flow_menu.grid(row=2, column=1, sticky=(tk.W + tk.E))
        if self._body_vars["UDP Flow"].get() != "":
            body_part = body_part + f'\n\tflow:"{self._body_vars["UDP Flow"].get()}";'
        
        # Set up all body options in format key:value
        if self._body_vars["Priority"].get() != "":
            body_part = body_part + f'\n\tpriority:{self._body_vars["Priority"].get()};'
        if self._body_vars["SID"].get() != "":
            body_part = body_part + f'\n\tsid:{self._body_vars["SID"].get()};'
        if self._body_vars["GID"].get() != "":
            body_part = body_part + f'\n\tgid:{self._body_vars["GID"].get()};'
        if self._body_vars["Revision Number"].get() != "":
            body_part = body_part + f'\n\trev:{self._body_vars["Revision Number"].get()};'

        body_part = body_part + "\n)"
        # Concatenate header and body
        self._vars["Rule"].set(f'{header_part}{body_part}')
    
    def _protocol_icmp(self, parent):
        # Set up header options: Action Protocol SrcIP -> DestIP
        header_part = f'{self._vars["Action"].get()} {self._vars["Protocol"].get()} {self._vars["Source IP"].get()} {self._vars["Direction"].get()} {self._vars["Destination IP"].get()}\n'
        # TODO: Type, Code
        body_part = "("
        if self._body_vars["Message"].get() != "":
            body_part = body_part + f'\n\tmsg:"{self._body_vars["Message"].get()}";'
        if self._body_vars["Class Type"].get() != "":
            body_part = body_part + f'\n\tclasstype:{self._body_vars["Class Type"].get()};'

        tk.Label(parent, text="").grid(row=0, column=0, sticky=(tk.W))
        tk.Label(parent, text="").grid(row=1, column=0, sticky=(tk.W))

        tk.Label(parent, text="ICMP Type").grid(row=2, column=0, sticky=(tk.W))
        icmp_type_entry = ttk.Entry(parent, textvariable=self._body_vars["ICMP Type"])
        icmp_type_entry.grid(row=2, column=1, sticky=(tk.W))
        if self._body_vars["ICMP Type"].get() != "":
            body_part = body_part + f'\n\titype:{self._body_vars["ICMP Type"].get()};'
        
        tk.Label(parent, text="ICMP Flow").grid(row=3, column=0, sticky=(tk.W))
        icmp_code_entry = ttk.Entry(parent, textvariable=self._body_vars["ICMP Code"])
        icmp_code_entry.grid(row=3, column=1, sticky=(tk.W))
        if self._body_vars["ICMP Code"].get() != "":
            body_part = body_part + f'\n\ticode:{self._body_vars["ICMP Code"].get()};'

        # Set up all body options in format key:value
        if self._body_vars["Priority"].get() != "":
            body_part = body_part + f'\n\tpriority:{self._body_vars["Priority"].get()};'
        if self._body_vars["SID"].get() != "":
            body_part = body_part + f'\n\tsid:{self._body_vars["SID"].get()};'
        if self._body_vars["GID"].get() != "":
            body_part = body_part + f'\n\tgid:{self._body_vars["GID"].get()};'
        if self._body_vars["Revision Number"].get() != "":
            body_part = body_part + f'\n\trev:{self._body_vars["Revision Number"].get()};'

        body_part = body_part + "\n)"
        # Concatenate header and body
        self._vars["Rule"].set(f'{header_part}{body_part}')
    
    def _prot_change(self, *_):
        prot_body = tk.Frame(self.b_info)
        for column in range(3):
            prot_body.columnconfigure(column, weight=1)
            
        if self._vars["Protocol"].get() == 'tcp':
            self._protocol_tcp(prot_body)
        elif self._vars["Protocol"].get() == 'udp':
            self._protocol_udp(prot_body)
        elif self._vars["Protocol"].get() == "icmp":
            self._protocol_icmp(prot_body)
        else:
            self._vars["Rule"].set('any -> any ()')
            
        prot_body.grid(row=1, column=2, columnspan=2, rowspan=5, sticky=(tk.N + tk.S + tk.E + tk.W))
            
        #self.rule_box._set_content()
        
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self._vars = dict()
        self._body_vars = dict()
        
        #Build the form
        self.columnconfigure(0, weight=1)
        
        # Rule Header info
        h_info = self._add_frame("Header Info", cols=7)
        
        ####################################### Line 1 #####################################
        
        # Action
        tk.Label(h_info, text="Action").grid(row=0, column=0, sticky=(tk.E + tk.W))
        #rule_action = tk.StringVar()
        self._vars["Action"] = tk.StringVar()
        action_menu = ttk.OptionMenu(h_info, self._vars["Action"], "alert", *m.action_options)
        action_menu.grid(row=1, column=0, sticky=(tk.E + tk.W))
        
        # Protocol
        tk.Label(h_info, text="Protocol").grid(row=0, column=1, sticky=(tk.E + tk.W))
        #rule_prot = tk.StringVar()
        self._vars["Protocol"] = tk.StringVar()
        prot_menu = ttk.OptionMenu(h_info, self._vars["Protocol"], "tcp", *m.protocol_options)
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
        self._vars["Direction"] = tk.StringVar()
        dir_menu = ttk.OptionMenu(h_info, self._vars["Direction"], "->", *m.direction_options)
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
        
        for key, value in self._vars.items():
            value.trace("w", self._prot_change)
        
        ############################################### Body Frame #####################################
        self.b_info = self._add_frame(self._vars["Protocol"].get().upper(), cols=4)
        
        # Message
        tk.Label(self.b_info, text="Message").grid(row=0, column=0, sticky=(tk.W))
        #rule_message = tk.StringVar()
        self._body_vars["Message"] = tk.StringVar()
        message_entry = ttk.Entry(self.b_info, textvariable=self._body_vars["Message"])
        message_entry.grid(row=0, column=1, columnspan= 3, sticky=(tk.E + tk.W))
        
        ######################### First Column #
        
        # Class Type
        tk.Label(self.b_info, text="Class Type").grid(row=1, column=0, sticky=(tk.W))
        #rule_classtype = tk.StringVar()
        self._body_vars["Class Type"] = tk.StringVar()
        classtype_entry = ttk.OptionMenu(self.b_info, self._body_vars["Class Type"], "unknown", *m.class_types)
        classtype_entry.grid(row=1, column=1, sticky=(tk.E + tk.W))
        
        # Priority
        tk.Label(self.b_info, text="Priority").grid(row=2, column=0, sticky=(tk.W))
        #rule_priority = tk.StringVar()
        self._body_vars["Priority"] = tk.StringVar()
        priority_menu = ttk.OptionMenu(self.b_info, self._body_vars["Priority"], "5", *m.priority_options)
        priority_menu.grid(row=2, column=1, sticky=(tk.E + tk.W))
        
        # SID
        tk.Label(self.b_info, text="SID").grid(row=3, column=0, sticky=(tk.W))
        #rule_sid = tk.StringVar(value="SID")
        self._body_vars["SID"] = tk.StringVar()
        sid_entry = ttk.Entry(self.b_info, textvariable=self._body_vars["SID"])
        sid_entry.grid(row=3, column=1, sticky=(tk.E + tk.W))
        
        # GID
        tk.Label(self.b_info, text="GID").grid(row=4, column=0, sticky=(tk.W))
        #rule_sid = tk.StringVar(value="SID")
        self._body_vars["GID"] = tk.StringVar()
        sid_entry = ttk.Entry(self.b_info, textvariable=self._body_vars["GID"])
        sid_entry.grid(row=4, column=1, sticky=(tk.E + tk.W))
        
        # Revision Number
        tk.Label(self.b_info, text="Revision number").grid(row=5, column=0, sticky=(tk.W))
        #rule_revnum = tk.StringVar(value="Rev Number")
        self._body_vars["Revision Number"] = tk.StringVar()
        revnum_entry = ttk.Entry(self.b_info, textvariable=self._body_vars["Revision Number"])
        revnum_entry.grid(row=5, column=1, sticky=(tk.E + tk.W))
        
        # TODO: Set up function that creates views for each protocol
        # Can have a function for each body which sets the view up, plus a "Controller" function 
        # that switches the view whenever the protocol changes
        # Make sure that there is a second function that *only* updates the rule box
        
        # Set default values for each protocol
        self._body_vars["HTTP Request"] = tk.StringVar(name="HTTP Request")
        self._body_vars["HTTP Request"].set("")
        #self._body_vars["HTTP Request"].trace_add("write", callback=self.http_callback)
        self._body_vars["HTTP Response"] = tk.StringVar(name="HTTP Response")
        self._body_vars["HTTP Response"].set("")
        #self._body_vars["HTTP Response"].trace_add("write", callback=self.http_callback)
        self._body_vars["Flags"] = tk.StringVar()
        self._body_vars["Flags"].set("")
        self._body_vars["TCP Flow"] = tk.StringVar()
        self._body_vars["TCP Flow"].set("")
        self._body_vars["UDP Flow"] = tk.StringVar()
        self._body_vars["UDP Flow"].set("")
        self._body_vars["ICMP Type"] = tk.StringVar()
        self._body_vars["ICMP Code"] = tk.StringVar()
        
        for key, value in self._body_vars.items():
            traceid = value.trace_add("write", self._prot_change)
            print(traceid)
        
        ############################################### Rule Frame #####################################
        
        r_info = self._add_frame("Rule", cols=1)
        
        self._vars["Rule"] = tk.StringVar()
        self.rule_box = w.BoundText(r_info, textvariable=self._vars["Rule"])
        self.rule_box.grid(row=0, column=0, sticky=(tk.N + tk.S + tk.E + tk.W))
        
        # We probably need separate functions to set up the body pseudo-views and to 
        # refresh the rule box, otherwise the variables in the second column reset 
        # anything anytime variables in the first column change
        self._prot_change()
        
        
        

        