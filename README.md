2Wire Bandwidth Monitoring
==========================
This is a quick and dirty Nagios-style script that I use to monitor bandwidth in and out of the 2Wire router used with my ATT Uverse internet connection

Dependencies
------------
Requires mechanize and BeautifulSoup, which you can install like so:

```bash    
easy_install mechanize    
easy_install BeautifulSoup
```
Use with Nagios/Zenoss
---------------
The monitoring system should be configured with COUNTER datasources. The script returns transmit_bytes and receive_bytes.

If the script is unable to hit your RG (default of 192.168.1.254), it will exit code 2, and tell you that it can't reach the gateway.
  