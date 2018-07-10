# shellshock-scan

shellshock-scan is a tiny script that automates the process of identifying and probing [ShellShock](https://www.cvedetails.com/cve/CVE-2014-6271/) vulnerable CGI scripts on Unix web servers. 

**The shellshock-scan project is sponsored by [CGI](https://www.cgi.com/en).**

Installation
----

You can download shellshock-scan by cloning the [Git](https://github.com/p33kab00/shellshock-scan) repository:

    git clone https://github.com/p33kab00/shellshock-scan.git

shellshock-scan works out of the box with [Python](http://www.python.org/download/) version **2.6.x** and **2.7.x** on any platform.

Usage
----

Identify and probe CGI scripts w/ approx 250 common scripts:

    $ python shellshock-scan.py http://192.168.5.138
    [*] shellshock-scan 0.1
    [*] by p33kab00 (mudnorb@gmail.com)
    [*] # of checks: 225
    
    [+] We've got a candidate: /cgi-bin/status
        Whoa - it's vulnerable!
    
    [*] Found 1 vulnerable scripts in 15901 ms.

Identify and probe CGI scripts on a host w/ a user-defined list of CGI-scripts:

    $ python shellshock-scan.py http://192.168.5.138 cgi-scripts.lst 
    [*] shellshock-scan 0.1
    [*] by p33kab00 (mudnorb@gmail.com)
    [*] # of checks: 1357
    
    [+] We've got a candidate: /cgi-bin/status
        Whoa - it's vulnerable!
    
    [*] Found 1 vulnerable scripts in 22623 ms.
