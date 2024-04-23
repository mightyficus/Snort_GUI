class menus:
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

    actions = [
        #'alert',
        'alert',
        'block',
        'drop',
        'log',
        'pass'
    ]

    protocols = [
        #'tcp',
        'tcp',
        'udp',
        'icmp'
    ]

    http_request_methods = [
        #"GET",
        "GET",
        "POST",
        "HEAD",
        "TRACE",
        "PUT",
        "DELETE",
        "CONNECT"
    ]

    http_codes = [
        # "200", "201", "204", "304", "400", "401",
        # "403", "404", "409", "410", "500"
        "100", "101",
        "200", "201", "202", "203", "204", "205", "206",
        "300", "301", "302", "303", "304", "305", "306", "307",
        "400", "401", "402", "403", "404", "405", "406", "407", "408", 
        "409", "410", "411", "412", "413", "415", "416", "417",
        "500", "501", "502", "503", "504", "505"
    ]

    flow = [
        "",
        "to_server",
        "to_client",
        "from_server",
        "from_client"
    ]

    icmp_types = [
        '0',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12',
        '13',
        '14',
        '15',
        '16',
        '17',
        '18',
        '30',
        '31',
        '32',
        '33',
        '34',
        '35',
        '36',
        '37',
        '38',
        '39',
        '40',
        '41',
        '42',
        '43'

    ]