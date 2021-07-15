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
