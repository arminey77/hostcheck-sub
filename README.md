# hostcheck

Check and validate host details:
+ Disk checks:
    + Partitions **&#x2611;**
    + LVM lists
    + Mounting
        + /var/log
        + NFS mount
    + Check /etc/fstab
+ Resource Check
    + CPU
    + Memory
+ Network
    + IP/Netmask Check
    + DNS
    + NTP **&#x2611;**
+ Sysbench
    + Resource Health Check
+ Check Accessibility for team users
+ Services:
    + Zabbix: service status (health check + service enabled)
    + Journald: set log size **&#x2611;**
    + SSHD: Increase SSH porcess priority


