# ModSecurity

## ModSecurity 소개
- 공개웹방화벽이며 오픈소스입니다. 
- 세계적으로 널리쓰이는 Apache 웹서버 모듈로서 통합되어 동작합니다.
- CLI(Command Line Interface) 기반입니다. 
- KISA에서 추천할 정도로 믿을만하고 지속적으로 업데이트가 잘 되고 있습니다.
- 경로, 파라미터분석 전에 정규화(Normalization) 시켜 우회 공격을 차단합니다.

## 네트워크 구성
- External network(192.168.10.0/24)   
Atacker(Kali-linux) : 192.168.10.50 (eth0)   
Firewall(CentOS) : 192.168.10.100 (eth0)   

- Intranet(192.168.20.0/24)   
Atacker(Kali-linux) : 192.168.20.50 (eth1)   
Firewall(CentOS) : 192.168.20.200 (eth1)   
Modsecurity+Apache Server(CentOS) : 192.168.20.203 (eth0) 

## ModSecurity 설치
- Apache version 확인
```
[root@modsecurity ~]# httpd -v
Server version: Apache/2.4.6 (CentOS)
Server built:   Nov 16 2020 16:18:20
```
- ModSecurity 설치
```
[root@modsecurity ~]# yum install mod_security -y
```
