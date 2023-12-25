#!/usr/bin/python3
from telnetlib import Telnet
from ansible.module_utils.basic import *

def telnet(dst: str, port: int, timeout=1):
    try:
        with Telnet(host=dst, port=port, timeout=timeout) as tn:
            return True
    except Exception as error:
        return False

def main():
    module = AnsibleModule(      
        {
            "dst": {"default": True, "type": "str"},
            "port": {"default": True, "type": "int"},
            "timeout": {"default": False, "type": "int"},
        }
    )
    access = telnet(module.params['dst'], module.params['port'], module.params['timeout'])
    module.exit_json(changed=not access, access=access)


if __name__ == '__main__':
    main()