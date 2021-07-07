# Hash
- 키(Key)와 값(Value)쌍으로 이루어진 데이터 구조를 의미합니다. Key를 이용하여 데이터를 찾으므로, 속도를 빠르게 만드는 구조입니다.
- 파이썬에서는 딕셔너리(Dictionary) 타입이 해쉬 테이블과 같은 구조입니다.
- 기본적으로는, 배열로 미리 Hash Table 크기만큼 생성해서 사용합니다. 
- 검색이 많이 필요한 경우, 저장, 삭제, 읽기가 많은 경우, 캐쉬를 구현할 때 주로 사용됩니다
- 시간 복잡도 - 일반적인 경우(충돌이 없는 경우) : O(1)
- 시간 복잡도 - 최악의 경우(모든 경우에 충돌이 발생하는 경우): O(n)
- 장점
  1. 데이터 저장/검색 속도가 빠릅니다.
  2. 해시는 키에 대한 데이터가 있는지(중복) 확인이 쉽습니다.
- 단점
  1. 일반적으로 저장공간이 좀더 많이 필요합니다.
  2. 여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요합니다. (충돌 해결 알고리즘)   
 
## Hash 용어 설명
![hash_description](/Algorithm/Hash/hash_description.png)
- 해쉬(Hash): 임의 값을 고정 길이로 변환하는 것을 의미합니다.
- 해시 함수(Hash Function): 특정 연산을 이용하여 키 값을 받아서 value를 가진 공간의 주소로 바꾸어주는 함수를 의미합니다.
- 해시 테이블(Hash Table): 해시 구조를 사용하는 데이터 구조입니다.
- 해시 값(해시 주소, Hash Value or Address): Key값을 해쉬 함수에 넣어서 얻은 주소값을 의미합니다. 이 값을 통해 슬롯을 찾아간다.
- 슬롯(Slot): 한 개의 데이터를 저장할 수 있는 공간을 의미합니다. (위 그림에서는 bucket)

## 해시 충돌
- Chaining 기법 : Open Hashing 기법 중 하나, 해시테이블 저장공간 외에 공간을 더 추가해서 사용하는 방법입니다. 충돌이 발생시, 링크드 리스트로 데이터를 추가로 뒤에 연결시키는 방법입니다.
- Linear Probing 기법 : Close Hashing 기법 중 하나, 해시 테이블 저장공간 안에서 충돌 문제를 해결하는 방법입니다. 충돌이 일어나면, 해당 hash value(hash address)의 다음 index부터 맨 처음 나오는 빈 공간에 저장하는 기법입니다. (저장 공간 활용도의 증가)

## 코딩 테스트

### 완주하지 못한 선수 (Level1)
- https://programmers.co.kr/learn/courses/30/lessons/42576
- 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
- https://github.com/HarkjinDev/Security/blob/main/Algorithm/Hash/hash_level1.py

### 전화번호 목록 (Level2)
- https://programmers.co.kr/learn/courses/30/lessons/42577
- 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
- https://github.com/HarkjinDev/Security/blob/main/Algorithm/Hash/hash_level2_1.py

### 위장 (Level2)
- https://programmers.co.kr/learn/courses/30/lessons/42578
- 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.
- https://github.com/HarkjinDev/Security/blob/main/Algorithm/Hash/hash_level2_2.py

### 베스트앨범 (Level3)
- https://programmers.co.kr/learn/courses/30/lessons/42579
- 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
- https://github.com/HarkjinDev/Security/blob/main/Algorithm/Hash/hash_level3.py
