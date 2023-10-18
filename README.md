# hostcheck

Check and validate host details:
+ Disk checks:
    + Partitions
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
    + NTP
+ Sysbench
    + Resource Health Check
+ Check Accessibility for team users
+ Services:
    + Zabbix: service status (health check + service enabled)
    + Journald: set log size
    + SSHD: Increase SSH porcess priority

