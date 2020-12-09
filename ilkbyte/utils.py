from enum import Enum


class PowerAction(str, Enum):
    start = "start"
    shutdown = "shutdown"
    reboot = "reboot"
    destroy = "destroy"


class DNSRecordType(str, Enum):
    A = 'A'
    AAAA = 'AAAA'
    CNAME = 'CNAME'
    MX = 'MX'
    TXT = 'TXT'
    NS = 'NS'
