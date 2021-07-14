# Graylog Server

## Graylog 소개
- Graylog는 MongoDB와 Elasticsearch를 기반으로 동작하며 사실상 로깅 수집과 분석을 타겟으로 제공되는 오픈소스기반이다.
- 설치가 간단하면서 다양한 인덱싱과 필터링 기반의 검색을 통해 값들을 그래프화 시킬 수 있다는 큰 장점이 있다.
- 리눅스 기반의 설치가 가능하며, 로그가 많은 경우 시스템의 메모리 및 Disk IO를 적절히 지원한다면 매우 유용한 로그 분석 솔루션이다.

## Graylog Server Architecture
![Graylog_Architecture](/Garylog/Graylog_Architecture.png)

## Graylog 구성 요소
- MongoDB - 구성정보, 메타정보 저장용으로 사용되는 DB
- Elasticsearch - Log 원격지에서 받은 로그 메세지를 저장하고 필요할 때 마다 검색할 수 있는 기능 제공. 용량이 많아지고 데이터 인덱싱을 위한 부하가 발생할 경우 고용량 메모리 및 High IOPS를 제공하는 저장 공간을 권고.
- Graylog server - 다양한 Input에서 발생하는 로그를 구문 분석하며, 해당 로그들을 처리할 수 있는 웹 인터페이스를 제공하는 서버

## Graylog 설치
