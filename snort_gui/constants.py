class Menus:
    action_options = [
            "alert",
            "block",
            "drop",
            "log",
            "pass"
        ]
    
    protocol_options = [
            "tcp",
            "udp",
            "icmp"
        ]
    
    direction_options = [
            "->",
            "<>"
        ]
    
    priority_options = [
        "5",
        "4",
        "3",
        "2",
        "1"
    ]
    
    class_types = [
        "unknown",
        "not-suspicious",
        "bad-unknown",
        "attempted-recon",
        "successful-recon-limited",
        "successful-recon-largescale",
        "attempted-dos",
        "successful-dos",
        "attempted-user",
        "unsuccessful-user",
        "successful-user",
        "attempted-admin",
        "successful-admin",
        "rpc-portmap-decode",
        "shellcode-detect",
        "string-detect",
        "suspicious-filename-detect",
        "suspicious-login",
        "system-call-detect",
        "tcp-connection",
        "trojan-activity",
        "unusual-client-port-connection",
        "network-scan",
        "denial-of-service",
        "non-standard-protocol",
        "protocol-command-decode",
        "web-application-activity",
        "misc-activity",
        "misc-attack",
        "icmp-event",
        "inappropriate-content",
        "policy-violation",
        "default-login-attempt",
        "sdf",
        "file-format",
        "malware-cnc",
        "client-side-exploit"
    ]
    
    http_codes = [
        "100", "101",
        "200", "201", "202", "203", "204", "205", "206",
        "300", "301", "302", "303", "304", "305", "306", "307",
        "400", "401", "402", "403", "404", "405", "406", "407", "408", 
        "409", "410", "411", "412", "413", "415", "416", "417",
        "500", "501", "502", "503", "504", "505"
    ]
    
    http_request_methods = [
        "GET",
        "POST",
        "HEAD",
        "TRACE",
        "PUT",
        "DELETE",
        "CONNECT"
    ]
    
    
    flow = [
        "to_server",
        "to_client",
        "from_server",
        "from_client"
    ]
    
    compare = [
        ">",
        "<",
        "=",
        "!=",
        "<=",
        ">="
    ]