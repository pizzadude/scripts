#!/usr/bin/python3
import os
import subprocess
with open("/proc/uptime", encoding="utf-8") as uptime_file:
        uptime, _ = uptime_file.read().strip().split()
        print(f"Uptime:  {float(uptime) // 3600} hour(s)")
encoding = 'utf-8'
seLinucks = subprocess.run(
    args = ["getenforce"],
    universal_newlines= False,
    stdout = subprocess.PIPE);
selinux = str(seLinucks.stdout, encoding)
selinux = selinux.strip()
print("SELinux:", selinux);
