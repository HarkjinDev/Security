# Splunk Example

## 	지난 60분 동안 서버에서 인증 실패가 발생했는지 확인
```
sourcetype=linux_secure fail* OR invalid | fields user, src_ip, app
```

## 중복 제거, 필드명 수정 후 테이블 형태로 저장
```
sourcetype=linux_secure fail* OR invalid | dedup user, src_ip | table user, src_ip, app | sort src_ip, user
```

## 직원들의 인터넷 사용현황 확인
```
sourcetype=cisco_wsa_squid | dedup username, usage | table username, usage | sort username
```

## 우리 사이트 방문자가 어느 사이트를 경유해서 오는지 확인
```
sourcetype=access_combined referer_domain!=http://home.com | top limit=3 refer_domain showperc=0
```

## 웹서버의 응답코드 분포 확인
```
sourcetype=access_combined | top limit=2 status by host showperc=0 | sort -count
```

## 직원들이 보는 컨텐츠 타입 중 드문 타입은 malicious 코드일 수 있으니 확인
```
sourcetype=cisco_wsa_squid | rare limit=3 cs_mime_type
```

# 지난 24시간동안 웹서버에서 발생한 인증 실패로그의 빈도를 security 대시보드에 컬럼 차트로 추가
```
sourcetype=linux_secure host=www* (vendor_action=failed OR vendor_action=“invalid user”) | chart count over vendor_action by src_ip useother=f
```

# 지난 7일 동안 북아메리카에서 가장 많이 팔린 제품을 국가별로 그룹핑하여 차트로 추가
```
sourcetype=vendor_sales VendorID<4000 | chart count over VendorCountry by product_name limit=5 userother=f
```

# 지난 24시간 동안 인터넷 사용을 security 대시보드에 라인 차트로 추가
```
sourcetype=cisco_wsa_squid | timechart count by usage
```

# 지난 7일 동안 웹서버에서 발생한 실패와 실패 트랜드 검색
```
sourcetype=linux_secure host=www* fail* | timechart count as failures | tendine sma2(failuers) as trend 
```

# 지난 7일 동안 미국에서 발생한 소매 판매 건수를 단계구분도에 표현
```
sourcetype=vendor_sales VendorID<3000 | chart count by VendorStateProvince | geom geo_us_states featureIDField=VendorStateProvince
```

# 이전 주 동안 국가별 온라인 판매 건수를 지도에 표현
```
sourcetype=access_combined action=purchase status=200 | iplocation clientip | geostats count by clientip
```

# 최근 24시간 동안 웹서버 별로 GET, POST 요청 비율 계산
```
sourcetype=access_combined | chart count over host by method | eval Ratio=round(GET/POST,2)
```

# 최근 4시간 동안 웹서버 로그인 실패가 3회 이상인 사용자를 확인하여 높은 순서로 정렬
```
sourcetype=linux_secure host=www* fail* | stats count by user | search count > 3 | sort -count
```

# 최근 7일 동안 직원들의 컨텐츠 타입별 웹트래픽 사용 현황 파악
```
sourcetype=cisco_wsa_squid | stats count by cs_mime_type | eval type=if(cs_mime_type LIKE “image%”, “graphic”, “other”) | stats sum(count) by type
```

# 최근 4시간 동안 www1, www2 웹서버의 웹로그에서 공통으로 발생한 status code 실패 이벤트 검색
```
host=www1 [search host=www2 (status >= 300 AND status < 600 | dedup status | fields status ] | dedup status | table status | sort status
```

# 최근 4시간 동안 www2에서는 발견되고, www1에서는 발견되지 않는 status code 실패 이벤트 검색
```
host=www2 ( status >= 300 AND status < 600 ) NOT [search host=www1 (status >= 300 AND status < 600 ) | dedup status | fields status] | dedup status | table status | sort status
```

# 최근 7일 동안 웹서버와 회사 네트워크 접속에서 동시에 패스워드 실패 이력이 있는 직원 확인
```
sourcetype=linux_secure fail* password [search sourcetype=winauthentication_security EventCode=4625 | dedup User | fields User | rename User as user] | stats values(host) by user
```
