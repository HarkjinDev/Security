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

## ModSecurity Rule
- /etc/httpd/conf.d/mod_security.conf
- SecRuleEngine On | Off | DetectionOnly   
  : ModSecurity 기능을 활성화 시킨다.   
  + DectectionOnly : 활성화는 하지만 차단하지 않고 탐지만 한다.
- SecAuditEngine On | Off | RelevantOnly   
  : 감사 로깅에 대한 설정을 구성한다.   
  + RelevantOnly : Error 또는 Warning의 트랜젝션, 그리고 SecAuditLogRelevantStatus에 정의된 상태코드와 일치하는 트렌젝션만 로깅
- SecAuditLog /var/log/httpd/modsec_audit.log   
  : 감사 로그 파일의 경로를 정의한다.
- SecAuditLogParts ABIJDEFHZ   
  : 로그 파일에 기록할 항목을 정의한다.
- SecAuditLogRelevantStatus REGEX   
  : 감사로깅의 목적과 관련된 response 상태코드의 값을 설정한다.
- SecAuditLogType Serial | Concurrent   
  : 감사로깅 구조의 타입을 설정한다.   
  + Serial : 모든 로그는 메인 로그파일에 저장된다. 하나의 파일에만 기록되기 때문에 느려질 수 있다.
  + Concurrent : 로그가 각 트랜젝션 별로 나누어 저장된다. 이 방식은 로그파일을 원격 ModSecurity Console Host로 보낼 때 사용하는 방식이다.
- SecDefaultAction "phase:1,deny,log"   
  : 룰이 매칭되면 기본적인 취할 행동을 정의한다.
  + Disruptive actions : ModSecurity가 데이터를 중간에서 가로챌 때 일어나는 행위이다. 하나의 체인에 첫 번째 룰에만 나타낼 수 있다. allow, deny, drop 등이 있다.
  + Non-Disruptive actions : 어디에나 나타날 수 있다. capture, ctl, exec, initcol 등이 있다.
  + Flow actions : 하나의 체인에 첫번째 rule에만 나타낼 수 있다. chain 등이 있다.
  + Meta-data actions : 하나의 체인에 첫번째 rule에만 나타낼 수 있다. id,rev,severity,msg 등이 있다.
  + Data actions : 전면적으로 수동적이고 다른 행위에서 사용된 데이터를 운반하는 역할뿐이다.

## ModeSecurity 모듈 적용
```
[root@modsecurity ~]# cd /etc/httpd/modsecurity.d
[root@modsecurity /etc/httpd/modsecurity.d]# git clone https://github.com/spiderLabs/owasp-modsecurity-crs.git
[root@modsecurity /etc/httpd/modsecurity.d]# cd owasp-modsecurity-crs/
[root@modsecurity /etc/httpd/modsecurity.d/owasp-modsecurity-crs]# cp crs-setup.conf.example crs-setup.conf
[root@modsecurity /etc/httpd/modsecurity.d/owasp-modsecurity-crs]# vi crs-setup.conf
SecDefaultAction “phase:1,log,auditlog,deny”
SecDefaultAction “phase:2,log,auditlog,deny”
[root@modsecurity ~]# vi /etc/httpd/conf.d/mod_security.conf 
Include modsecurity.d/owasp-modsecurity-crs/crs-setup.conf
Include modsecurity.d/owasp-modsecurity-crs/rules/*.conf
SecRuleEngine On
SecAuditEngine On
SecDebugLogLevel 5
```
