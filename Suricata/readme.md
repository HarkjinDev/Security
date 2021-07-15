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

## Suritaca Log 실습
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

## Ping of Death 공격 로그
- Suritaca rule 생성 및 적용
```
┌──(root💀ids)-[~/]
└─# vi /etc/suricata/rules/local.rules
alert icmp any any -> $HOME_NET any (msg: "PING Alret"; sid:1000001; rev:1;)

┌──(root💀ids)-[~/]
└─# vi /etc/suricata/suricata.yaml
rule-files:
  - suricata.rules
  - local.rules
  
┌──(root💀ids)-[~]
└─# systemctl restart suricata
```
- Attacker Ping of death 공격 (참고 : https://github.com/HarkjinDev/Security/blob/main/Python/pingofdeath.py )
```
┌──(root💀kali)-[~]
└─# python pingofdeath.py 192.168.20.134 100
```
- 로그 확인
```
┌──(root💀ids)-[~/]
└─# tail -f /var/log/suricata/fast.log 
07/15/2021-17:13:09.546283  [**] [1:1000001:1] PING Alret [**] [Classification: (null)] [Priority: 3] {ICMP} 192.168.20.50:8 -> 192.168.20.134:0
07/15/2021-17:13:09.546404  [**] [1:1000001:1] PING Alret [**] [Classification: (null)] [Priority: 3] {ICMP} 192.168.20.134:0 -> 192.168.20.50:0
07/15/2021-17:13:11.876573  [**] [1:1000001:1] PING Alret [**] [Classification: (null)] [Priority: 3] {ICMP} 192.168.20.134:11 -> 192.168.20.50:1
07/15/2021-17:13:11.876593  [**] [1:1000001:1] PING Alret [**] [Classification: (null)] [Priority: 3] {ICMP} 192.168.20.134:11 -> 192.168.20.50:1
```
