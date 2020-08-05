## KNN(K-Nearest Neighbor) 알고리즘
가장 간단한 분류 알고리즘

### 소개
```
오렌지와 자몽이 있다. 크기가 크고 붉으면 자몽, 크기가 작고 오렌지색이면 오렌지이다.
크기가 중간이고 색상이 붉은색과 주황색 중간인 과일이 있다. 이 과일은 오렌지인가 자몽인가?
```
* 이 과일을 분류하는 방법으로, 그래프상에서 주변을 둘러보는 방법이 있다.
* 이 과일의 주변 가장 가까운 이웃(neighbor)이 3개 있다.
* 이웃 2개는 오렌지, 이웃 1개는 자몽이다.
* 따라서 이 과일은 오렌지일 것이다.
> 이 분류 과정이 KNN 알고리즘이다.

### 추천 시스템 만들기
```
모든 고객을 그래프 상에 나타낸다. 유사도(similarity)를 이용하여 취향이 비슷한 고객을 근접한 위치에 그린다.
어떤 고객을 위해 영화를 추천해야 할 때, 취향이 가장 비슷한 5명의 고객을 찾는다.
해당 고객들이 좋아한 영화를 추천한다.
```
##### 분류
유사한 고객끼리 모으기(그룹으로 나누기)

* 특징 추출
    - 추천하고자 하는 영화와 직접 관련이 있는 특징
    - 편향되지 않은 특징(이 경우에는 코미디 영화에 대한 평점만 있는 등.)
* 유클리디언 거리
    - 2차원 이상의 공간에서 거리는 두 집합의 유사도를 뜻한다.
> 고객이 더 많은 영화를 평가할수록 넷플릭스는 나와 다른 고객의 유사도를 더 정확하게 평가할 수 있다. 그래서 영화 평가해달란 공지가 나오는 것임.
##### 회귀 분석
숫자로 된 반응 예측하기

* 내가 어떤 영화에 대해 어떤 평점을 줄지 예측할 수 있을까?
    > 가장 유사한 5명일 필요는 없다. 2명일수도, 10명일수도, 1000명일 수도 있다. 그래서 알고리즘 이름이 KNN(K-Nearest negihbor)이다.
* 평점을 예측하고자 하는 영화 A가 있다. 이 영화를 나와 가장 유사한 5명의 고객의 평점을 계산한다.
    > 이것을 회귀(regression)분석이라 한다.

### OCR(Optical Character Recognition)
책의 페이지를 사진으로 찍으면 그 사진 속의 글자를 읽어주는 것.

* 사진으로 찍은 숫자 7이 무슨 숫자인지 어떻게 알 수 있을까?
    1. 여러가지 숫자 그림을 살펴보고 이 그림들의 특징을 뽑는다.(traning 과정)
    2. 새로운 그림이 그려지면 그 그림의 특징을 뽑아서 가장 가까운 것들을 살펴본다.
> 실제 ocr에서 사용되는 특징의 추출은 자몽 오렌지 문제보다 훨씬 복잡하지만, 아무리 복잡한 기술이라도 KNN과 같은 간단한 아이디어에 기반하고 있다.

### 스팸 필터
나이브 베이즈 분류기 사용

* 나이브 베이즈 분류기를 트레이닝
    ```
    패스워드를 설정하세요 | not spam
    백만 달러를 벌어보세요 | spam
    패스워드를 보내주세요 | spam
    당신에게 천만불을 보냈습니다 | spam
    생일 축하합니다 | not spam
    ```
* ```백만 달러를 벌어보세요!```라는 제목의 이메일은 스팸일까 아닐까?
    - 위 문장을 단어로 쪼갠다.
    - 각 단어마다 그 단어가 스팸 메일에 나타날 확률을 구한다.