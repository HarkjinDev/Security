# Programmers SQL

https://programmers.co.kr/learn/challenges?tab=sql_practice_kit

## SELECT 
### 모든 레코드 조회하기 (Level1)
- 동물 보호소에 들어온 모든 동물의 정보를 ANIMAL_ID순으로 조회하는 SQL문을 작성해주세요.
```sql
SELECT *
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```
### 역순 정렬하기 (Level2)
- 동물 보호소에 들어온 모든 동물의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 ANIMAL_ID 역순으로 보여주세요. SQL을 실행하면 다음과 같이 출력되어야 합니다.
```sql
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC
```
### 
