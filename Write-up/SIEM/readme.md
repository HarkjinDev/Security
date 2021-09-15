# SIEM(Security Information & Event Management)
- Security Onion v2 및 취약한 서버로 인프라 구축
- 각종 해킹툴을 사용한 다양한 취약점 진단 및 분석
- ELK 및 Splunk를 이용하여 보안 이벤트 분석 및 시각화

# 네트워크 구성도
![network](/Write-up/SIEM/networkdiagram.png)

Pfsense (Firewall)
- WAN-em0Wan-em0(ens33) : 192.168.10.3
- Lan-em1(ens34) : 192.168.20.3
- Em2(ens35) : 192.168.30.3

SeucrityOnion v2
- em0(ens33) : 192.168.10.5/24
- em1(ens34) : 192.168.20.5/24

Splunk(Ubuntu)
- em0(ens33) : 192.168.10.6/24
- em1(ens34) : 192.168.20.6/24

