## Chapter 8. 탐욕 알고리즘(Greedy)
불가능한 문제, 즉 빠른 알고리즘 해법이 존재하지 않는 문제를 다루는 법, 빠른 알고리즘을 찾느라 시간을 낭비하지 않도록 문제 해결이 불가능한지 아닌지 파악하는 방법.


### 탐욕 알고리즘 소개
* 수업 시간표 짜기 문제: 최대한 많은 수업을 듣고 싶을 때
* 해법: 탐욕 알고리즘
    1. 가장 빨리 끝나는 과목을 처음으로 신청한다.
    2. 첫 번째 과목이 끝난 후 시작하는 과목 중, 가장 빨리 끝나는 과목을 찾아 신청한다.
* 탐욕 알고리즘은 간단하다. 각각의 단계에서 최적의 수를 찾으면 된다.
* 기술적 용어로는, 각 단계에서 국소 최적해(locally optimal solution)을 찾음으로써 최종적으로 전역 최적해(globally optimal solution)을 찾을 수 있다.
* 탐욕 알고리즘이 항상 성공하는 것은 아니다.
* 그러나 탐욕 알고리즘은 구현히 간단하면서도 **보통은 정답에 상당히 가까운 답을 준다.**
* 따라서 탐욕 알고리즘은 근사 알고리즘(approximation algorithm)으로 사용된다.
    * 근사 알고리즘의 성능: 1.얼마나 빠른가 2.최적화에 얼마나 가까운가

### 집합 커버링 문제(Set-covering problem)
* set() : 리스트를 집합으로 바꿈.
    * 집합은 중복된 원소를 가지지 않는다.
* 집합 연산
    * & 교집합
    * | 합집합
    * - 차집합

### NP-완전문제(NP-complete problem)
* 외판원 문제와 집합 커버링 문제는 모든 가능한 경우를 다 따져서 최단/최소를 구해야 한다. 이런 문제를 NP-완전문제라 한다.
* NP-완전문제임을 알면, 문제를 완벽하게 풀려는 노력을 멈추고 근사 알고리즘을 써서 문제를 풀 수 있다.
* 그러나 어떻게 알지?
    * 몇 가지 고려사항
    > 항목이 적을땐 알고리즘이 빠른데, 항목이 늘어나면서 급격히 느려질 때
    
    > ```X의 모든 조합```이라고 하면 보통 NP-완전문제
    
    > 더 작은 하위 문제로 변환할 수 없어서 X의 가능한 모든 버전을 계산해야 할 때
    
    > 문제가 수열(외판원 문제와 같은 도시의 순서처럼)을 포함하고 풀기가 어려울 때
    
    > 문제에 집합(라디오 방송국 집합처럼)이 있고 풀기가 어려울 때
    
    > 문제를 집합 커버링 문제나 외판원 문제로 재정의할 수 있다면, 명백하게 NP-완전문제이다.
