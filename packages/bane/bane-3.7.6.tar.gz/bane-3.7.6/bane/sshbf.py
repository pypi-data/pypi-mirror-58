try:
 import paramiko
 from paramiko import SSHClient, AutoAddPolicy
except:
 pass
try:
 import pexpect
except:
 pass
import subprocess
def ssh_linux(u,username,password,p=22,timeout=7):
 p='ssh -o StrictHostKeyChecking=no -p {} {}@{}'.format(p,username,u)#the command to spawn with "expect" on linux
 #command="echo ala_is_king"
 # "StrictHostKeyChecking=no" option was added to add the host automatically
 try:
  child = pexpect.spawn(p)
  usr=False
  while True:
   try:
    child.expect(['.*:'],timeout=timeout)#read until it reads ":"
   except:
    pass
   c=child.before
   c+= child.after
   c=str(c)
   #if "yes/no" in c:
    #child.send('yes\n')
   if (('login:' in c.lower()) or ('username:' in c.lower())):
    if usr==True:
       break
    child.send(username+'\n')#send username
    usr=True
   elif "password:" in c.lower():
    child.send(password+'\n')#send password
    break
   else:
    break
  #child.send(command+'\n')
  try:
   child.expect('.*=.*',timeout=timeout)#wait reading unexisting character in the prompt
  except:
   pass
  c= child.before
  c=str(c)
  child.close()
  if (('username:' not in c.lower()) and ('login:' not in c.lower()) and ("password:" not in c.lower())):
   for x in ['#','$','>']:
    if x in c:#if the shell was accessed successfully
     if ((c.count('#')<2) or (c.count('>')<2) or (c.count('$')<2)):
      return True
 except Exception as e:
  pass
 return False
def ssh_win(ip,username,password,p=22,timeout=5):
 #ssh login for windows
 try:
  s = SSHClient()
  s.set_missing_host_key_policy(AutoAddPolicy())
  s.connect(ip, p,username=username, password=password,timeout=timeout)
  stdin, stdout, stderr = s.exec_command ("echo ala_is_king",timeout=timeout)
  r=stdout.read()
  s.close()
  if "ala_is_king" in str(r):# paramiko sometimes returns a false positive results so we execute the echo command and check the result to verify the login
   return True
 except Exception as e:
  pass
 return False
def ssh_andro(u,username,password,timeout=5):
 # ssh login on termux
 l="sshpass -p {} ssh -o ConnectTimeout={} -o StrictHostKeyChecking=no {}@{} echo ala_is_king; exit".format(password,timeout,username,u)
 #we use the "sshpass" command to send the password or the password prompt will pop up
 ssh = subprocess.Popen(l.split(),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 p= ssh.communicate()
 try:
   ssh.kill()
 except:
   pass
 if str(p[0]).strip()=='ala_is_king':
  return True
 else:
  return False
