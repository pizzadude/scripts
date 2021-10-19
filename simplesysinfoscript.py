#!/usr/bin/python3
import os
import subprocess
hoursUptime = subprocess.run(
    args = ["/home/pizzadude/bin/pythonscripts/uptimehours.sh"],
    universal_newlines= False,
    stdout = subprocess.PIPE);
encoding = 'utf-8'
hu = str(hoursUptime.stdout, encoding)
hu = hu.strip()
print("Uptime:","", hu ,"hours");
seLinucks = subprocess.run(
    args = ["getenforce"],
    universal_newlines= False,
    stdout = subprocess.PIPE);
selinux = str(seLinucks.stdout, encoding)
selinux = selinux.strip()
print("SELinux:", selinux);
