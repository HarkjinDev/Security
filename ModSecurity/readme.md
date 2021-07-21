# ModSecurity

## ModSecurity 소개
- 공개 웹방화벽이며 오픈소스입니다. 
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
- ModSecurity 설치 (ModSecurity v2.x 설치)
```
[root@modsecurity ~]# yum install mod_security mod_security_crs -y
```

## ModSecurity 설정
- /etc/httpd/conf.d/mod_security.conf : modsecurity 주설정 파일
- /etc/httpd/modsecurity.d/*.conf : CSR(Core Rule Set) 파일들
- /etc/httpd/modsecurity.d/activated_rules/*.conf : CSR(Core Rule Set) 파일들
```
[root@modsecurity ~]# tree /etc/httpd/
/etc/httpd/
├── conf.d
│   ├── mod_security.conf
├── modsecurity.d
│   ├── activated_rules
│   └── modsecurity_crs_10_config.conf
```
- WAF 기능 ON
```
[root@modsecurity ~]# vi /etc/httpd/conf.d/mod_security.conf 
SecRuleEngine On
```

## ModSecurity 로그 확인
- /var/log/httpd/modsec_debug.log : 디버그 로그 파일
- /var/log/httpd/modsec_audit.log : 감사 로그 파일
```
[root@modsecurity ~]# tree /var/log/httpd/
/var/log/httpd/
├── modsec_audit.log
├── modsec_debug.log
```
```
[root@modsecurity ~]# tail -f /var/log/httpd/modsec_audit.log
[root@modsecurity ~]# tail -f /var/log/httpd/modsec_debug.log
```
