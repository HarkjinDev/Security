# Suricata IDS

## Suritaca 소개
- 오픈소스 기반의 IDS 
- 멀티 코어(Multicore)/멀티 스레드 (Multi-threading) 완벽 지원
- Snort 룰 완벽 호환 및 기능 모두 지원
- 하드웨어 밴더의 개발 지원으로 하드웨어 가속 지원 (GPU 가속)
- 스크립터 언어(lua)로 시그니처 작성 가능

## 네트워크 구성
- External network(192.168.10.0/24)   
Atacker(Kali-linux) : 192.168.10.50 (eth0)   
Firewall(CentOS) : 192.168.10.100 (eth0)   

- Intranet(192.168.20.0/24)   
Atacker(Kali-linux) : 192.168.20.50 (eth1)   
Firewall(CentOS) : 192.168.20.200 (eth1)   
IDS(Kali-linux/Suricata) : 192.168.20.60 (eth0)   
WEB Server(Metasploitable v2) : 192.168.20.134 (eth0)   

## Suricata 설치
```
┌──(root💀ids)-[~]
└─# apt-get update

┌──(root💀ids)-[~]
└─# apt list "suricata*"
suricata-oinkmaster/kali-rolling 1:6.0.1-2 all
suricata-update/kali-rolling 1.2.1-1 amd64
suricata/kali-rolling 1:6.0.1-2 amd64

┌──(root💀ids)-[~]
└─# apt-get -y install suricata jq
```

## Suricata 설정 및 기동
```
┌──(root💀ids)-[~]
└─# vi /etc/suricata/suricata.yaml
#HOME_NET: "[192.168.0.0/16,10.0.0.0/8,172.16.0.0/12]"
HOME_NET: "[192.168.20.0/24]"

┌──(root💀ids)-[~]
└─# systemctl enable --now suricata
```

## Suricata 로그 확인
- suricata.log : 기동 정보 파일
```
┌──(root💀ids)-[~]
└─# tail -f /var/log/suricata/suricata.log
```
- stats.log : 통계 정보 파일
```
┌──(root💀ids)-[~]
└─# tail -f /var/log/suricata/stats.log
```
- fast.log : 규칙에 해당되는 기록을 남기는 파일
```
┌──(root💀ids)-[~]
└─# tail -f /var/log/suricata/fast.log
```
- eve.json : EVE JSON 파일
```
┌──(root💀ids)-[~]
└─# tail -f /var/log/suricata/eve.json
```

## Suricata Rule
- Rule 업데이트
```
┌──(root💀ids)-[~]
└─# suricata-update

┌──(root💀ids)-[~]
└─# suricata-update update-sources
```
- Rule List
```
┌──(root💀ids)-[~]
└─# suricata-update list-sources 
```
- Rule Test
```
┌──(root💀ids)-[~]
└─# suricata -T
```
- Rule 활성화
```
┌──(root💀ids)-[~]
└─# suricata-update enable-source oisf/trafficid
```
- 활성화 된 Rule List
```
┌──(root💀ids)-[~]
└─# suricata-update list-enabled-sources
Enabled sources:
  - et/open
  - oisf/trafficid
```
- Rule 비활성화
```
┌──(root💀ids)-[~]
└─# suricata-update disable-source oisf/trafficid
```
- Rule Source 제거
```
┌──(root💀ids)-[~]
└─# suricata-update remove-source oisf/trafficid 
```

## Paros webproxy 로그
- Suritaca 설정
```
┌──(root💀ids)-[~]
└─# vi /etc/suricata/suricata.yaml 
rule-files:
  - suricata.rules
  - app-layer-events.rules
  - decoder-events.rules
  - dhcp-events.rules
  - dnp3-events.rules
  - dns-events.rules
  - files.rules
  - http-events.rules
  - ipsec-events.rules
  - kerberos-events.rules
  - modbus-events.rules
  - nfs-events.rules
  - ntp-events.rules
  - smb-events.rules
  - smtp-events.rules
  - stream-events.rules
  - tls-events.rules

classification-file: /etc/suricata/classification.config
reference-config-file: /etc/suricata/reference.config

┌──(root💀ids)-[~]
└─# cp /var/lib/suricata/rules/classification.config /etc/suricata/

┌──(root💀ids)-[~]
└─# cp /var/lib/suricata/rules/suricata.rules /etc/suricata/rules/  

┌──(root💀ids)-[~]
└─# systemctl restart suricata
```
- Attacker 정상 테스트
```
┌──(root💀kali)-[~]
└─# ping -c 3 192.168.20.134

┌──(root💀kali)-[~]
└─# nmap -p 22 192.168.20.134

┌──(root💀kali)-[~]
└─# firefox http://192.168.20.134 &
```
- Suricata 로그 확인 : Attacker의 정상 request 이므로 특별한 로그는 없음.
```
┌──(root💀ids)-[~]
└─# tail -f /var/log/suricata/fast.log 
```
- Attacker Paros spider(Firefox는 local proxy 활성화)
```
┌──(root💀kali)-[~]
└─# paros &

┌──(root💀kali)-[~]
└─# firefox 192.168.20.134 &
```
- Suricata 로그 확인
```
┌──(root💀ids)-[~]
└─# tail -f /var/log/suricata/fast.log 
[**] ET WEB_SERVER ColdFusion administrator access [**] [Classification: Web Application Attack] [Priority: 1] {TCP} 192.168.20.100:38971 -> 192.168.20.134:80
```

## Ping of Death 공격 및 로그
- Suricata rule 생성 및 적용
```
┌──(root💀ids)-[~/]
└─# vi /etc/suricata/rules/local.rules
alert icmp any any -> $HOME_NET any (msg:"## Ping of Death ##"; content:"|5858585858|"; sid:1000001; rev:1;)

┌──(root💀ids)-[~/]
└─# vi /etc/suricata/suricata.yaml
rule-files:
  - local.rules
  
┌──(root💀ids)-[~]
└─# systemctl restart suricata
```
- Attacker Ping of death 공격
```
┌──(root💀kali)-[~]
└─# hping3 -1 --rand-source 192.168.20.134 -d 50 --flood  
```
- Suricata 로그 확인
```
┌──(root💀ids)-[~/]
└─# tail -f /var/log/suricata/fast.log 
[**] [1:1000001:1] ## Ping of Death ## [**] [Classification: (null)] [Priority: 3] {ICMP} 42.46.244.26:8 -> 192.168.20.134:0
```

## ICMP Flooding 공격 및 로그
- Suricata rule 생성 및 적용
```
┌──(root💀ids)-[~]
└─# vi /etc/suricata/rules/local.rules                                                                                                 
alert icmp any any -> $HOME_NET any (msg:"## ICMP Flooding ##"; itype:8; threshold:type both, track by_dst, count 100, seconds 2; sid:2017032607; rev:1;)

┌──(root💀ids)-[~]
└─# systemctl restart suricata
```
- ICMP Flooding 공격
```
┌──(root💀kali)-[~/]
└─# hping3 -1 192.168.20.134 --flood
```
- Suricata 로그 확인
```
┌──(root💀ids)-[~]
└─# tail -f /var/log/suricata/fast.log 
[**] [1:2017032607:1] ## ICMP Flooding ## [**] [Classification: (null)] [Priority: 3] {ICMP} 192.168.20.50:8 -> 192.168.20.134:0
```

## XMAS Scanning 로그
- Suricata rule 생성 및 적용
```
┌──(root💀ids)-[~/]
└─# vi /etc/suricata/rules/local.rules
alert tcp any any -> $HOME_NET any (msg:"## SCAN XMAS ##"; flags: FPU,12; sid:2017032605; rev:1;)

┌──(root💀ids)-[~]
└─# systemctl restart suricata
```
- XMAS Scanning
```
┌──(root💀kali)-[~/]
└─# nmap -sX -p 21 192.168.20.134
```
- Suricata 로그 확인
```
┌──(root💀ids)-[~/
└─# tail -f /var/log/suricata/fast.log 
[**] [1:2017032605:1] ## SCAN XMAS ## [**] [Classification: (null)] [Priority: 3] {TCP} 192.168.20.50:40697 -> 192.168.20.134:21
```

## WEB 공격 로그
- Suricata rule 생성 및 적용
```
┌──(root💀ids)-[~]
└─# vi /etc/suricata/rules/local.rules                                                                                                 
alert tcp any any -> $HOME_NET 80 (msg:"## WAF - wafw00f ##"; content: "/cmd.exe"; nocase; http_uri; sid:2017032609; rev:1;)

┌──(root💀ids)-[~]
└─# systemctl restart suricata
```
- wafw00f Attack
```
┌──(root💀kali)-[~/]
└─# wafw00f http://192.168.20.134
```
- Suricata 로그 확인
```
┌──(root💀ids)-[~]
└─# tail -f /var/log/suricata/fast.log 
[**] [1:2017032609:1] ## WAF - wafw00f ## [**] [Classification: (null)] [Priority: 3] {TCP} 192.168.20.50:51744 -> 192.168.20.134:80
```
## OS Command Injection 공격
- Suricata rule 생성 및 적용

- OS Command Injection

- Suricata 로그 확인

## SQL Injection 공격
- Suricata rule 생성 및 적용

- SQL Injection

- Suricata 로그 확인

## XSS Injection 공격
- Suricata rule 생성 및 적용

- XSS Injection

- Suricata 로그 확인
