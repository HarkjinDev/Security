# Programmers SQL

https://programmers.co.kr/learn/challenges?tab=sql_practice_kit

## SELECT 
### 모든 레코드 조회하기 (Level1)
- https://programmers.co.kr/learn/courses/30/lessons/59034
- 동물 보호소에 들어온 모든 동물의 정보를 ANIMAL_ID순으로 조회하는 SQL문을 작성해주세요.
```sql
SELECT *
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```
### 역순 정렬하기 (Level1)
- https://programmers.co.kr/learn/courses/30/lessons/59035
- 동물 보호소에 들어온 모든 동물의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 ANIMAL_ID 역순으로 보여주세요.
```sql
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC
```
### 아픈 동물 찾기 (Level1)
- https://programmers.co.kr/learn/courses/30/lessons/59036
- 동물 보호소에 들어온 동물 중 아픈 동물의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요.
```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION='Sick'
```
### 어린 동물 찾기 (Level1)
- https://programmers.co.kr/learn/courses/30/lessons/59037
- 동물 보호소에 들어온 동물 중 젊은 동물1의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요.
```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
```
### 동물의 아이디와 이름 (Level1)
- https://programmers.co.kr/learn/courses/30/lessons/59403
- 동물 보호소에 들어온 모든 동물의 아이디와 이름을 ANIMAL_ID순으로 조회하는 SQL문을 작성해주세요.
```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```
### 여러 기준으로 정렬하기 (Level1)
- https://programmers.co.kr/learn/courses/30/lessons/59404
- 동물 보호소에 들어온 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회하는 SQL문을 작성해주세요. 단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여줘야 합니다.
- 이름을 사전 순으로 정렬하면 다음과 같으며, 'Jewel', 'Raven', 'Sugar'
- 'Raven'이라는 이름을 가진 개와 고양이가 있으므로, 이 중에서는 보호를 나중에 시작한 고양이를 먼저 조회합니다.
```sql
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME ASC, DATETIME DESC
```
### 상위 n개 레코드 (Level1)
- https://programmers.co.kr/learn/courses/30/lessons/59405
- 동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문을 작성해주세요.
```sql
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1
```

## SUM, MAX, MIN
### 최대값 구하기 (Level1)
- https://programmers.co.kr/learn/courses/30/lessons/59415
- 가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.
```sql
SELECT MAX(DATETIME)
FROM ANIMAL_INS
```
### 최솟값 구하기 (Level2)
- https://programmers.co.kr/learn/courses/30/lessons/59038
- 동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.
```sql
SELECT MIN(DATETIME)
FROM ANIMAL_INS
```
### 동물 수 구하기 (Level2)
- https://programmers.co.kr/learn/courses/30/lessons/59406
- 동물 보호소에 동물이 몇 마리 들어왔는지 조회하는 SQL 문을 작성해주세요.
```sql
SELECT COUNT(ANIMAL_ID) AS count
FROM ANIMAL_INS
```
### 중복 제거하기 (Level2)
- https://programmers.co.kr/learn/courses/30/lessons/59408
- 동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL 문을 작성해주세요. 이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다.
```sql
SELECT COUNT(A.NAME) AS count
FROM (SELECT NAME FROM ANIMAL_INS GROUP BY NAME) AS A
WHERE NAME IS NOT NULL 
```

## GROUP BY
### 고양이와 개는 몇 마리 있을까 (Level2)
- https://programmers.co.kr/learn/courses/30/lessons/59040
- 동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.
```sql
SELECT ANIMAL_TYPE, COUNT(*) AS count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE
```
### 동명 동물 수 찾기 (Level2)
- https://programmers.co.kr/learn/courses/30/lessons/59041
- 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.
```sql
SELECT NAME, COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT > 1
ORDER BY NAME
```
### 입양 시각 구하기(1) (Level2)
- https://programmers.co.kr/learn/courses/30/lessons/59412
- 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
```sql
SELECT HOUR(DATETIME), COUNT(*) AS COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) < 20
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME)
```
### 입양 시각 구하기(2) (Level4)
- https://programmers.co.kr/learn/courses/30/lessons/59413
- 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
- Tip) 변수 사용시 SET이 아닌 쿼리문에서는 반드시 대입 연산자(assignment operator := )를 사용
```sql
SET @HOUR = -1;
SELECT (@HOUR := @HOUR +1) AS HOUR, (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @HOUR) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR < 23
```

## IS NULL
### 이름이 없는 동물의 아이디 (Level1)
- https://programmers.co.kr/learn/courses/30/lessons/59039
- 동물 보호소에 들어온 동물 중, 이름이 없는 채로 들어온 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.
```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID
```
### 이름이 있는 동물의 아이디 (Level1)
- https://programmers.co.kr/learn/courses/30/lessons/59407
- 동물 보호소에 들어온 동물 중, 이름이 있는 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.
```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
ORDER BY ANIMAL_ID
```
### NULL 처리하기 (Level2)
- https://programmers.co.kr/learn/courses/30/lessons/59410
- 입양 게시판에 동물 정보를 게시하려 합니다. 동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 
- 이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 "No name"으로 표시해 주세요.
```sql
SELECT ANIMAL_TYPE, IFNULL(NAME, "No name") AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
```

## JOIN
### 없어진 기록 찾기 (Level3)
- https://programmers.co.kr/learn/courses/30/lessons/59042
- 천재지변으로 인해 일부 데이터가 유실되었습니다. 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.
```sql
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS AS A
RIGHT JOIN ANIMAL_OUTS AS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.ANIMAL_ID IS NULL
```
### 있었는데요 없었습니다. (Level3)
- https://programmers.co.kr/learn/courses/30/lessons/59043
- 관리자의 실수로 일부 동물의 입양일이 잘못 입력되었습니다. 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 
- 이때 결과는 보호 시작일이 빠른 순으로 조회해야합니다.
```sql
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS AS A
JOIN ANIMAL_OUTS AS B
ON B.ANIMAL_ID = A.ANIMAL_ID
WHERE B.DATETIME < A.DATETIME
ORDER BY A.DATETIME
```
### 오랜 기간 보호한 동물(1) (Level3)
- https://programmers.co.kr/learn/courses/30/lessons/59044
- 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 
- 이때 결과는 보호 시작일 순으로 조회해야 합니다.
```sql
SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS AS A
LEFT JOIN ANIMAL_OUTS AS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
ORDER BY A.DATETIME
LIMIT 3
```
### 보호소에서 중성화한 동물 (Level4)
- https://programmers.co.kr/learn/courses/30/lessons/59045
- 보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다. 보호소에 들어올 당시에는 중성화1되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.
```sql
SELECT B.ANIMAL_ID, B.ANIMAL_TYPE, B.NAME
FROM ANIMAL_INS AS A
JOIN ANIMAL_OUTS AS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.SEX_UPON_INTAKE != B.SEX_UPON_OUTCOME
ORDER BY A.ANIMAL_ID
```

## String, Date
### 루시와 엘라 찾기 (Level2)
- https://programmers.co.kr/learn/courses/30/lessons/59046
- 동물 보호소에 들어온 동물 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디와 이름, 성별 및 중성화 여부를 조회하는 SQL 문을 작성해주세요.
- 이때 결과는 아이디 순으로 조회해주세요.
```sql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty")
ORDER BY ANIMAL_ID
```
### 이름에 el이 들어가는 동물 찾기 (Level2)
- https://programmers.co.kr/learn/courses/30/lessons/59047
- 동물 보호소에 들어온 동물 이름 중, 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 
- 이때 결과는 이름 순으로 조회해주세요. 단, 이름의 대소문자는 구분하지 않습니다.
```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE "%EL%" AND ANIMAL_TYPE = "Dog"
ORDER BY NAME
```
