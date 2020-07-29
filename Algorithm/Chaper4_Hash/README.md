## Chapter 5. 해시 테이블
### 해시 함수의 소개
```
식료품 가게에서 일을 하고 있다고 생각해 보자. 손님이 물건을 사러 오면 모든 물건의 가격이 적혀 있는 가격 장부에서 가격을 찾아봐야 한다.
가격 장부가 식료품 이름 순으로 정렬되어 있다면 O(logN)시간이 걸릴 것이다(이진 탐색).
이진 탐색은 매우 빠르지만, 출납 업무를 하는데 있어 매번 장부를 확인하는 것은 힘들다. 가격을 찾는 동안 다른 손님이 몰려들어 올 것이다. 나는 모든 물건의 가격과 이름을 외우고 있는 동료가 필요하다. 그 동료의 이름은 '해시 함수'이다.
```

### 해시 함수
* 해시 함수: 문자열을 받아서 숫자를 반환하는 함수.
* 해시 함수는 문자열에 대해 숫자를 할당(mapping) 한다.
* 특징
    - 일관성: 만약 'apple'을 넣었을 때 4를 반환한다면 'apple'을 넣을 때마다 반환하는 값은 항상 4여야 한다.
        - 해시 함수는 같은 문자열에 대해서는 항상 같은 인덱스를 할당한다.
    - 무결성: 다른 단어가 들어가면 다른 숫자를 반환한다. 아주 조금이라도 다른 데이터라면 다른 값을 반환해야 한다.
        - 해시 함수는 다른 문자열에 대해서는 다른 인덱스를 할당한다.
        - 해시 함수는 배열의 크기를 알고 있어야 하며 유요한 인덱스만 반환해야 한다.

### 해시 테이블
* 해시 함수와 배열을 합친 구조. key: value의 구조를 가진다.
* Hash map(java), map(JS), **dictionary(Python)**, associative array라는 이름으로도 알려져 있다.
    ```
    JSON 또한 key: value의 자료구조 형태를 가지는 데이터이다.
    JSON은 소켓통신, XML 이후에 등장한 구조로, 값을 파싱하여 해석할 필요가 없어 simple하여 굉장히 널리 쓰인다. 따라서 다양한 언어에서 해당 자료구조를 제공한다.
    ```
* 언제 사용하는 것이 좋을까?
    - 어떤 것을 다른 것과 연관시키고자 할 때
    - 무언가를 찾아보고자 할 때
    - 중복된 항목을 방지할 때
* 해시 테이블 사용 예
    - DNS: 웹 주소(도메인)에 대해 IP를 할당하는 DNS 프로토콜에서 해시가 사용된다.
    - 캐싱(cache): 웹 페이지가 캐싱하는 자료들은 해시 테이블에 저장된다.

## 충돌(collision)
```
첫 글자에 따라 공간을 할당하는 해시 테이블을 만들었다.
Apple은 첫 공간에, Banana는 두 번째 공간에 할당되어 각각의 가격을 갖는다.
Avocado를 해시에 넣고 싶은데, 이미 Apple이 공간을 차지하고 있다(충돌). 충돌이 발생하면 Avocado가 Apple을 덮어쓰게 되고, Apple의 가격을 찾을 때 Avocado의 가격이 나온다.
```
* 해결 방법
    - 같은 공간에 여러 개의 키를 연결 리스트로 만들어 넣는다.
        - 연결 리스트가 길어지면 해시 테이블의 속도가 느려진다.
    - 이상적인 해시 함수를 만들어야 한다.
        - 예시의 해시 함수는 A로 시작하는 모든 키를 하나에 할당하는 해시 함수이다. 이상적인 해시 함수는 키를 해시 테이블 전체에 고르게 할당해야 한다.
    - **즉, 충돌을 피하기 위해서는 낮은 사용률과 좋은 해시 함수가 필요하다.**
* 사용률(load factor)
    ```
    해시 테이블에 있는 항목의 수 / 해시 테이블에 있는 공간의 수
    ```
    * 100개의 물건 가격을 해시 테이블에 저장할 때 100개의 공간이 필요하다. 최선의 경우에는 모든 항목이 자기 공간을 따로 가지며, 이 때 사용률은 1이다.
    * 해시 테이블의 공간이 50일 경우 사용률은 2이다.
    ```
    즉, 사용률이 1보다 크다는 것은 배열에 공간의 수보다 항목의 수가 많다는 뜻이다.
    ```
    * resizing: 사용률이 커지기 시작하면 해시 테이블의 공간을 추가해야 한다.
* 좋은 해시 함수
    * 배열에 값을 고루 분포시키는 함수.