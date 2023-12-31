#!/usr/bin/python3
from telnetlib import Telnet
from ansible.module_utils.basic import *
import dns.resolver
import logging

logging.basicConfig(level=logging.DEBUG)

def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


def telnet(dst: str, port: int, timeout=1):
    try:
        with Telnet(host=dst, port=port, timeout=timeout) as tn:
            return True
    except Exception as error:
        logging.error('Error on telnet %s', error)
        return False

def main():

    module = AnsibleModule(
        {
            "dst": {"default": True, "type": "str"},
            "port": {"default": True, "type": "int"},
            "timeout": {"default": False, "type": "int"},
        }
    )
    logging.info('Arguments: %s', module.params)
    # Check IP format
    if validate_ip(module.params['dst']):
        logging.debug('Dst has IP format')
        access = telnet(module.params['dst'], module.params['port'], module.params['timeout'])
        module.exit_json(changed=not access, access=access)
    # Domain Format
    else:
        logging.debug('Dst has DOMAIN format')
        access_returns = []
        try:
            ips = dns.resolver.query(module.params['dst'], 'A')
            logging.debug('list of A records for %s: %s', module.params['dst'], [ip.to_text() for ip in ips])
            for ip in ips:
                logging.debug(ip)
                access_returns.append(telnet(str(ip), module.params['port'], module.params['timeout']))
            logging.debug(all(access_returns))
            module.exit_json(changed=not all(access_returns), access=all(access_returns))
        except Exception as e:
            logging.error('Error on DNS resolver %s', e)

if __name__ == '__main__':
    main()