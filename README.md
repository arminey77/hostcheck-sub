# hostcheck

Check and validate host details:
+ Add default apt repo list
+ Disk checks:
    + Partitions **&#x2611;**
    + LVM lists **&#x2611;**
    + Mounting
        + /var/log
        + NFS mount
    + Check /etc/fstab
+ Resource Check
    + CPU **&#x2611;**
    + Memory **&#x2611;**
+ Network
    + IP/Netmask Check **&#x2611;**
    + DNS
+ Sysbench
    + Resource Health Check
+ Check Access Lists **&#x2611;**
+ Services:
    + Timesyncd(similar to NTP) **&#x2611;**
    + Zabbix Agent: service status (health check + service enabled)
    + Splunk Agent: service status (health check + service enabled)
    + Journald: set log size **&#x2611;**
    + SSHD: Increase SSH porcess priority


## Access Check

+ Ping all:
```
ansible -K -k -i ../inventory -e 'ansible_user=<YOUR_USER>@<ENV_DOMAIN>' -m ping all
```

+ Check all access lists:
```
ansible-playbook -K -k -i ../inventory main.yml -b -e 'ansible_user=<YOUR_USER>@<ENV_DOMAIN>' -t access_check
```

+ Check access lists of specific host:
```
ansible-playbook -K -k -i ../inventory main.yml -b -e 'ansible_user=<YOUR_USER>@<ENV_DOMAIN>' -t access_check -l "<HOST>"
```

+ Check single access (Use `access_check.yml` playbook):
```
ansible-playbook -K -k -i ../inventory access_check.yml -b -e 'ansible_user=<YOUR_USER>@<ENV_DOMAIN>' -t access_check -l "<HOST>" -e "access_check_single=<IP/DOMAIN>:<PORT>"
```