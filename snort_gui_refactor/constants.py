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
        'alert',
        'alert',
        'block',
        'drop',
        'log',
        'pass'
    ]

    protocols = [
        'tcp',
        'tcp',
        'udp',
        'icmp'
    ]