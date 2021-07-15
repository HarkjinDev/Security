# Suricata IDS

## 네트워크 구성
- External network(192.168.10.0/24)   
Atacker(Kali-linux) : 192.168.10.50 (eth0)   
Firewall(CentOS) : 192.168.10.100 (eth0)   

- Intranet(192.168.20.0/24)   
Atacker(Kali-linux) : 192.168.20.50 (eth1)   
Firewall(CentOS) : 192.168.20.200 (eth1)   
IDS(Suritaca) : 192.168.20.60 (eth0)   
WEB Server(Metasploitable v2) : 192.168.20.134 (eth0)   

## Suricata 설치
