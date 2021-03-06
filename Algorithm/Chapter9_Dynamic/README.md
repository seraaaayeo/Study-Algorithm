## Chapter 9. 동적 프로그래밍(Dynamic programming)
어려운 문제를 여러 개의 하위 문제로 쪼개고, 이 하위 문제들을 먼저 해결하는 방법

### 소개
```
배낭 채우기 문제
4파운드의 짐을 넣을 수 있는 배낭을 가지고 있고, 훔칠 수 있는 물건은 3개가 있다.
각 물건은 무게와 가격이 다르다.
최대한 물건의 가치가 최대치로 높게 훔칠 수 있는 방법은?
```
* Greedy 알고리즘을 사용하여 근사해를 구하면 최적해에 가깝긴 하지만, 최적해는 아닐 수도 있다. 최적해는 어떻게 계산할 수 있을까?
* 동적 프로그래밍

### 특징
* 동적 프로그래밍은 각 하위 문제들이 서로 관계가 없을 때, 즉 의존하지 않는 경우에만 쓸 수 있다.
* 어떤 제한 조건이 주어졌을 때 무언가를 최적화하는 경우에 유용하다.
    * 예를 들어, 배낭 채우기 문제에서 제한 조건은 배낭의 크기, 최적화 목표는 훔칠 물건의 총 가치를 최대화하는 것이다.