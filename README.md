# shellshock-scan

shellshock-scan is an open source penetration testing tool that automates the process of identifying and probing ShellShock (CVE-2014-6271) vulnerable CGI scripts on Unix web servers. 

**The shellshock-scan project is sponsored by [CGI](https://www.cgi.com/en).**

Installation
----

You can download shellshock-scan by cloning the [Git](https://github.com/p33kab00/shellshock-scan) repository:

    git clone --depth 1 https://github.com/p33kab00/sqlmap.git sqlmap-dev

shellshock-scan works out of the box with [Python](http://www.python.org/download/) version **2.6.x** and **2.7.x** on any platform.

Usage
----

Identify and probe CGI scripts on a host w/ approx 250 common scripts:

    python shellshock-scan.py http://10.10.10.10

Identify and probe CGI scripts on a host w/ user supplied file of scripts:

    python shellshock-scan.py http://10.10.10.10 /usr/share/wordlist/cgi-scripts.lst
