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



## Notes:
+ Ping all:
```
ansible -K -k -i ../inventory -e 'ansible_user=<YOUR_USER>@<ENV_DOMAIN>' -m ping all
```