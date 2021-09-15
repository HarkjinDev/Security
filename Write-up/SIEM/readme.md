# SIEM(Security Information & Event Management)
- Security Onion v2 및 취약한 서버로 인프라 구축
- 각종 해킹툴을 사용한 다양한 취약점 진단 및 분석
- ELK 및 Splunk를 이용하여 보안 이벤트 분석 및 시각화

# 네트워크 구성도
![network](/Write-up/SIEM/networkdiagram.png)

Pfsense (Firewall)
- WAN-em0(ens33) : 192.168.10.3
- LAN-em1(ens34) : 192.168.20.3

SeucrityOnion v2
- em0(ens33) : 192.168.10.5/24
- em1(ens34) : 192.168.20.5/24

Splunk(Ubuntu)
- em0(ens33) : 192.168.10.6/24
- em1(ens34) : 192.168.20.6/24

# Security Onion 설치
- Administrative username : analyst
- Choose install type : EVAL (Evaluation mode)
- Elastic Stack Lincense: AGREE
- Manager install : Standard
- Hostname : so-eval
- Network Configuration : ens33
- IP : 192.168.10.5/24
- Gateway : 192.168.10.1
- DNS : 8.8.8.8
- Internet connect : Direct
- Monitor Interface Network Configuration : ens34
- OS patch schedule : Automatic
- Home network : (default)
- Components Install : ALL Check (default)
- Default Docker IP range : Yes
- Web Interface : analyst@example.com
- Web Interface access : HOSTNAME
- NTP Sever : Yes
- Web tools allow access : Yes
- CIDR Single IP range : 192.168.10.0/24
- Reference : https://blog.securityonion.net/2020/12/security-onion-2321-now-available.html

# Security Onion 설정
## 방화벽 해제
- sudo systemctl sotp firewalld

## Suricata
- sudo so-suricata-start
- sudo so-suricata-stop
- /opt/so/log/suricata/suricata.log
- /opt/so/log/suricata/stats.log
- /opt/so/conf/suricata/suricata.yaml
- /opt/so/saltstack/default/salt/suricata/defaults.yaml
- HOMENET 설정
```
[analyst@so-eval ~]$ sudo vim /opt/so/saltstack/local/pillar/global.sls
global:
3   hnmanager: '192.168.10.0/24, 192.168.20.0/24'

[analyst@so-eval ~]$ sudo salt-call state.apply suricata
```
- Rule 파일
```
[analyst@so-eval ~]$ sudo tree /opt/so/saltstack/local/salt/suricata/rules
├── all.rules
├── local.rules
└── sorules
    ├── extraction.rules
    └── filters.rules
```
- Rule 수정
```
[analyst@so-eval ~]$ sudo vim /opt/so/saltstack/local/salt/idstools/local.rules
[analyst@so-eval ~]$ sudo so-rule-update
```

# Kibana

# Kibana 시각화

# Splunk 설치

# Splunk 
