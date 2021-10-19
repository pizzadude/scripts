#!/usr/bin/python3
import os
import subprocess
import math
with open("/proc/uptime", encoding="utf-8") as uptime_file:
        uptime, _ = uptime_file.read().strip().split()
        up = math.trunc(float(uptime))
        print(f"Uptime:  {up // 3600} hour(s)")
encoding = 'utf-8'
seLinucks = subprocess.run(
    args = ["getenforce"],
    universal_newlines= False,
    stdout = subprocess.PIPE);
selinux = str(seLinucks.stdout, encoding)
selinux = selinux.strip()
print("SELinux:", selinux);
