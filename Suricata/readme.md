# Suricata IDS

## Suritaca 소개
- 오픈소스 기반의 IDS 
- 멀티 코어(Multicore)/멀티 스레드 (Multi-threading) 완벽 지원
- Snort 룰 완벽 호환 및 기능 모두 지원
- 하드웨어 밴더의 개발 지원으로 하드웨어 가속 지원. (GPU 가속)
- 스크립터 언어(lua)로 시그니처 작성 가능

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
