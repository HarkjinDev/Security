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
- SecDefaultAction "phase:1,deny,log"   
  : 룰이 매칭되면 기본적인 취할 행동을 정의한다.
  + Disruptive actions : ModSecurity가 데이터를 중간에서 가로챌 때 일어나는 행위이다. 하나의 체인에 첫 번째 룰에만 나타낼 수 있다. allow, deny, drop 등이 있다.
  + Non-Disruptive actions : 어디에나 나타날 수 있다. capture, ctl, exec, initcol 등이 있다.
  + Flow actions : 하나의 체인에 첫번째 rule에만 나타낼 수 있다. chain 등이 있다.
  + Meta-data actions : 하나의 체인에 첫번째 rule에만 나타낼 수 있다. id,rev,severity,msg 등이 있다.
  + Data actions : 전면적으로 수동적이고 다른 행위에서 사용된 데이터를 운반하는 역할뿐이다.
  + allow : rule에 매칭되면 처리를 멈추고 트랜젝션을 허가한다.
  + drop : FIN 패킷을 보내 TCP 연결을 끊어서 연결을 종료시킨다.
  + deny : rule이 일치할 경우 요청 처리를 차단한다.
  + exec : 필터가 일치하면 파라미터를 지원하는 외부 스크립트/바이너리를 실행시킨다.
  + log : 필터가 일치하였을 때 로그를 남긴다.
- SecDebugLogLevel 0|1|2|3|4|5|6|7|8|9   
  : 디버그 로그의 상세 수준을 결정한다.
- SecDataDir /var/lib/mod_security   
  : 영구적 데이터를 저장할 경로를 지정한다.
- SecTmpDir /var/lib/mod_security   
  : 임시 파일이 생성될 디렉토리를 설정한다.

## ModeSecurity OWASP 모듈 적용
- OWASP crs 다운 및 적용
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

[root@modsecurity ~]# systemctl restart httpd.service
```
- Host IP 접속 제한 풀기
```
[root@modsecurity ~]#vi /etc/httpd/modsecurity.d/owasp-modsecurity-crs/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf
#SecRule REQUEST_HEADERS:Host "@rx ^[\d.:]+$" \
#    "id:920350,\
#    phase:2,\
#    block,\
#    t:none,\
#    msg:'Host header is a numeric IP address',\
#    logdata:'%{MATCHED_VAR}',\
#    tag:'application-multi',\
#    tag:'language-multi',\
#    tag:'platform-multi',\
#    tag:'attack-protocol',\
#    tag:'paranoia-level/1',\
#    tag:'OWASP_CRS',\
#    tag:'OWASP_CRS/PROTOCOL_VIOLATION/IP_HOST',\
#    tag:'WASCTC/WASC-21',\
#    tag:'OWASP_TOP_10/A7',\
#    tag:'PCI/6.5.10',\
#    ver:'OWASP_CRS/3.2.0',\
#    severity:'WARNING',\
#    setvar:'tx.anomaly_score_pl1=+%{tx.warning_anomaly_score}'"
```
- Attacker Command Injection 진행 및 로그 확인
```
[root@modsecurity ~]# tail -f /var/log/httpd/modsec_audit.log 
Message: Access denied with code 403 (phase 2). Matched phrase "etc/passwd" at ARGS:ip. [file "/etc/httpd/modsecurity.d/owasp-modsecurity-crs/rules/REQUEST-930-APPLICATION-ATTACK-LFI.conf"] [line "99"] [id "930120"] [msg "OS File Access Attempt"] [data "Matched Data: etc/passwd found within ARGS:ip: & cat /etc/passwd"] [severity "CRITICAL"] [ver "OWASP_CRS/3.2.0"] [tag "application-multi"] [tag "language-multi"] [tag "platform-multi"] [tag "attack-lfi"] [tag "paranoia-level/1"] [tag "OWASP_CRS"] [tag "OWASP_CRS/WEB_ATTACK/FILE_INJECTION"] [tag "WASCTC/WASC-33"] [tag "OWASP_TOP_10/A4"] [tag "PCI/6.5.4"]
Apache-Error: [file "apache2_util.c"] [line 271] [level 3] [client 192.168.20.50] ModSecurity: Access denied with code 403 (phase 2). Matched phrase "etc/passwd" at ARGS:ip. [file "/etc/httpd/modsecurity.d/owasp-modsecurity-crs/rules/REQUEST-930-APPLICATION-ATTACK-LFI.conf"] [line "99"] [id "930120"] [msg "OS File Access Attempt"] [data "Matched Data: etc/passwd found within ARGS:ip: & cat /etc/passwd"] [severity "CRITICAL"] [ver "OWASP_CRS/3.2.0"] [tag "application-multi"] [tag "language-multi"] [tag "platform-multi"] [tag "attack-lfi"] [tag "paranoia-level/1"] [tag "OWASP_CRS"] [tag "OWASP_CRS/WEB_ATTACK/FILE_INJECTION"] [tag "WASCTC/WASC-33"] [tag "OWASP_TOP_10/A4"] [tag "PCI/6.5.4"] [hostname "192.168.20.203"] [uri "/dvwa/vulnerabilities/exec/"] [unique_id "YPe@z8Z98KBfm1XIsBoc-gAAAAI"]
Action: Intercepted (phase 2)
```
- Attacker SQL Injection 진행 및 로그 확인
```
[root@modsecurity ~]# tail -f /var/log/httpd/modsec_audit.log 
Message: Access denied with code 403 (phase 2). detected SQLi using libinjection with fingerprint '1&1' [file "/etc/httpd/modsecurity.d/owasp-modsecurity-crs/rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf"] [line "68"] [id "942100"] [msg "SQL Injection Attack Detected via libinjection"] [data "Matched Data: 1&1 found within ARGS:id: 1\x19 or \x181\x19=\x191"] [severity "CRITICAL"] [ver "OWASP_CRS/3.2.0"] [tag "application-multi"] [tag "language-multi"] [tag "platform-multi"] [tag "attack-sqli"] [tag "paranoia-level/1"] [tag "OWASP_CRS"] [tag "OWASP_CRS/WEB_ATTACK/SQL_INJECTION"] [tag "WASCTC/WASC-19"] [tag "OWASP_TOP_10/A1"] [tag "OWASP_AppSensor/CIE1"] [tag "PCI/6.5.2"]
Apache-Error: [file "apache2_util.c"] [line 271] [level 3] [client 192.168.20.50] ModSecurity: Access denied with code 403 (phase 2). detected SQLi using libinjection with fingerprint '1&1' [file "/etc/httpd/modsecurity.d/owasp-modsecurity-crs/rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf"] [line "68"] [id "942100"] [msg "SQL Injection Attack Detected via libinjection"] [data "Matched Data: 1&1 found within ARGS:id: 1\\\\x19 or \\\\x181\\\\x19=\\\\x191"] [severity "CRITICAL"] [ver "OWASP_CRS/3.2.0"] [tag "application-multi"] [tag "language-multi"] [tag "platform-multi"] [tag "attack-sqli"] [tag "paranoia-level/1"] [tag "OWASP_CRS"] [tag "OWASP_CRS/WEB_ATTACK/SQL_INJECTION"] [tag "WASCTC/WASC-19"] [tag "OWASP_TOP_10/A1"] [tag "OWASP_AppSensor/CIE1"] [tag "PCI/6.5.2"] [hostname "192.168.20.203"] [uri "/dvwa/vulnerabilities/sqli/"] [unique_id "YPfA5WF6mFOASudccjwUjAAAAAQ"]
Action: Intercepted (phase 2)
```

## ModSecurity Rule 개발
- 로컬 룰을 위한 설정(local.conf)
```
[root@modsecurity ~]# vi /etc/httpd/conf.d/mod_security.conf
Include modsecurity.d/*.conf
#Include modsecurity.d/activated_rules/*.conf
SecRuleEngine On
SecDefaultAction "phase:1,deny,log"
SecDebugLogLevel 5

[root@modsecurity ~]# cd /etc/httpd/modsecurity.d
[root@modsecurity /etc/httpd/modsecurity.d]# mv modsecurity_crs_10_config.conf modsecurity_crs_10_config.conf.old
[root@modsecurity /etc/httpd/modsecurity.d]# touch local.conf

[root@modsecurity ~]# systemctl restart httpd.service
```
- Command Injection 룰 설정
```
[root@modsecurity ~]# vi /etc/httpd/modsecurity.d/local.conf 
SecRule ARGS ";[[:space:]]*(ls|pwd|wget|cd|id|cat)" "phase:2,deny,rev:'2',msg:'Command execution attack',id:'0000000001',skipAfter:END_COMMAND_INJECTION1"
SecMarker END_COMMAND_INJECTIOON1

[root@modsecurity ~]# systemctl restart httpd.service
```
- Command Injection 공격 및 로그 확인
```
[root@modsecurity ~]# tail -f /var/log/httpd/modsec_audit.log 
Message: Access denied with code 403 (phase 2). Pattern match ";[[:space:]]*(ls|pwd|wget|cd|id|cat)" at ARGS:ip. [file "/etc/httpd/modsecurity.d/local.conf"] [line "1"] [id "0000000001"] [rev "2"] [msg "Command execution attack"]
```
- SQL Injection 룰 설정
```
[root@modsecurity ~]# vi /etc/httpd/modsecurity.d/local.conf
SecRule ARGS "\' or \'1=1" "phase:2,deny,rev:'1',msg:'SQL Injection Attack',id:'0000000002',skipAfter:END_SQL_INJECTION1"
SecRule ARGS "\'[[:space:]].*or.*\'1[[:space:]]*=[[:space:]]*1" "phase:2,deny,rev:'1',msg:'SQL Injection Attack',id:'0000000003',skipAfter:END_SQL_INJECTION1"
SecMarker END_SQL_INJECTION1
```
- SQL Injection 공격 및 로그 확인
```
[root@modsecurity ~]# tail -f /var/log/httpd/modsec_audit.log 
Message: Access denied with code 403 (phase 2). Pattern match "\\' or \\'1=1" at ARGS:id. [file "/etc/httpd/modsecurity.d/local.conf"] [line "6"] [id "0000000002"] [rev "1"] [msg "SQL Injection Attack"]
Apache-Error: [file "apache2_util.c"] [line 271] [level 3] [client 192.168.20.50] ModSecurity: Access denied with code 403 (phase 2). Pattern match "\\\\\\\\' or \\\\\\\\'1=1" at ARGS:id. [file "/etc/httpd/modsecurity.d/local.conf"] [line "6"] [id "0000000002"] [rev "1"] [msg "SQL Injection Attack"] [hostname "192.168.20.203"] [uri "/dvwa/vulnerabilities/sqli/"] [unique_id "YPfHg4y0-@-IOi7ehZyMIwAAAAE"]
Action: Intercepted (phase 2)
```
- XSS 룰 설정
```
[root@modsecurity ~]# vi /etc/httpd/modsecurity.d/local.conf 
SecRule ARGS "<[[:space:]]*script*>.*script[[:space:]]*>" "phase:2,deny,rev:'1',msg:'XSS Attack',id:'0000000004',skipAfter:END_XSS_ATTACK1"
SecMarker END_XSS_ATTACK1
```
- XSS 공격 및 로그 확인
```
[root@modsecurity ~]# tail -f /var/log/httpd/modsec_audit.log 
Message: Access denied with code 403 (phase 2). Pattern match "<[[:space:]]*script*>.*script[[:space:]]*>" at ARGS:name. [file "/etc/httpd/modsecurity.d/local.conf"] [line "11"] [id "0000000004"] [rev "1"] [msg "XSS Attack"]
Apache-Error: [file "apache2_util.c"] [line 271] [level 3] [client 192.168.20.50] ModSecurity: Access denied with code 403 (phase 2). Pattern match "<[[:space:]]*script*>.*script[[:space:]]*>" at ARGS:name. [file "/etc/httpd/modsecurity.d/local.conf"] [line "11"] [id "0000000004"] [rev "1"] [msg "XSS Attack"] [hostname "192.168.20.203"] [uri "/dvwa/vulnerabilities/xss_r/"] [unique_id "YPfIGLmZmWlJiU4mqBa6hgAAAAE"]
Action: Intercepted (phase 2)
```

## ModSecurity 가이드 (By Kisa)
https://www.boho.or.kr/data/secNoticeView.do?bulletin_writing_sequence=21488   
Kisa Rule1 (소기업) :    
Kisa Rule2 (중기업) :   
