#!/bin/bash
echo $(awk '{print $1}' /proc/uptime) / 3600 | bc
