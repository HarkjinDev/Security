# Graylog Server

## Graylog 소개
- Graylog는 MongoDB와 Elasticsearch를 기반으로 동작하며 사실상 로깅 수집과 분석을 타겟으로 제공되는 오픈소스기반이다.
- 설치가 간단하면서 다양한 인덱싱과 필터링 기반의 검색을 통해 값들을 그래프화 시킬 수 있다는 큰 장점이 있다.
- 리눅스 기반의 설치가 가능하며, 로그가 많은 경우 시스템의 메모리 및 Disk IO를 적절히 지원한다면 매우 유용한 로그 분석 솔루션이다.

## Graylog Server Architecture
![Graylog_Architecture](/Graylog/Garylog_Architecture.png)

## Graylog 구성 요소
- MongoDB - 구성정보, 메타정보 저장용으로 사용되는 DB
- Elasticsearch - Log 원격지에서 받은 로그 메세지를 저장하고 필요할 때 마다 검색할 수 있는 기능 제공. 용량이 많아지고 데이터 인덱싱을 위한 부하가 발생할 경우 고용량 메모리 및 High IOPS를 제공하는 저장 공간을 권고.
- Graylog server - 다양한 Input에서 발생하는 로그를 구문 분석하며, 해당 로그들을 처리할 수 있는 웹 인터페이스를 제공하는 서버

## Graylog 설치
### 1. 필요 패키지 설치
```
[root@linux ~]# yum install epel-release -y
```
```
[root@linux ~]# yum install wget pwgen -y
```
```
[root@linux ~]# yum install java-1.8.0-openjdk-headless.x86_64 -y
```

### 2. MongoDB 설치 및 기동
```
[root@linux ~]# vi /etc/yum.repos.d/mongodb.repo 
[mongodb-org-4.0]
name = MongoDB Repository
baseurl = https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.0/x86_64/
gpgcheck = 1
enabled = 1
gpgkey = https://www.mongodb.org/static/pgp/server-4.0.asc
```
```
[root@linux ~]# yum install mongodb-org -y
```
```
[root@linux ~]# systemctl enable --now mongod
```

### 3. Elasticsearch 설치 및 설정
GPG키 임포트
```
[root@linux ~]# rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
```
패키지 설치
```
[root@linux ~]# vi /etc/yum.repos.d/elasticsearch.repo 
[elasticsearch-6.x]
name=Elasticsearch repository for 6.x packages
baseurl=https://artifacts.elastic.co/packages/oss-6.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
```
```
[root@linux ~]# yum install elasticsearch-oss -y
```
설정 파일 수정
```
[root@linux ~]# vi /etc/elasticsearch/elasticsearch.yml 
cluster.name: graylog
```
서비스 기동
```
[root@linux ~]# systemctl enable --now elasticsearch
```
동작 점검
```
[root@linux ~]# curl -XGET 'http://localhost:9200'
  "cluster_name" : "graylog",
```
```
[root@linux ~]# curl -XGET 'http://localhost:9200/_cluster/health?pretty=true'
  "cluster_name" : "graylog",
  "status" : "green",
```
### 4. Graylog Server 설치
```
[root@linux ~]# rpm -Uvh https://packages.graylog2.org/repo/packages/graylog-3.0-repository_latest.rpm
[root@linux ~]# yum -y install graylog-server
```
계정 패스워드 암호화 및 설정 파일 수정
```
[root@linux ~]# echo -n "Enter Password: " && head -1 </dev/stdin | tr -d '\n' | sha256sum | cut -d" " -f1
Enter Password: admin
8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
```
```
[root@linux200 ~]# pwgen -N 1 -s 96
n2NJ5r1CS652LaqI3rAgnXmvXfMhPVZAQPcOc9HzyYaRVmRUxStb5tOV3eI3bsktSEWl3PrEvw4d8egoqSSOn3HxK7g5joGS
```
```
[root@linux ~]# vi /etc/graylog/server/server.conf 
root_timezone = Asia/Seoul
elasticsearch_shards = 1
password_secret = n2NJ5r1CS652LaqI3rAgnXmvXfMhPVZAQPcOc9HzyYaRVmRUxStb5tOV3eI3bsktSEWl3PrEvw4d8egoqSSOn3HxK7g5joGS
root_password_sha2 = 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
```
