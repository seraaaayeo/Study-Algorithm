'''
그래프 해시 테이블 생성
key: 그래프의 정점
val: 이웃 정점의 정보. 
     {이웃 정점: 가격}. 즉, 이웃하는 모든 정점의 이름과 가격을 해시 테이블로 갖는다.
'''
graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
#print(graph["start"].keys()) #dict_keys(['a', 'b'])
#print(graph["start"]["a"]) #6

graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["fin"] = 5
graph["b"]["a"] = 3

graph["fin"] = {} #최종 거리값을 넣을 해시 테이블 생성

'''
가격에 대한 해시 테이블
키: 정점 
val: 가격
'''
infinity = float("inf") #가격을 모르는 정점의 가격은 무한대로 둔다.
costs={}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

'''
부모를 나타내는 해시 테이블
key: 정점
val: 해당 정점의 부모 정점.
'''
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

'''
이미 처리한 정점을 추적하기 위한 배열 선언
'''
processed = []

'''
알고리즘 시작
'''
def find_min_cost_node(costs):
    min_cost = float("inf")
    min_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < min_cost and node not in processed:
            min_cost = cost
            min_cost_node = node
    return min_cost_node

node = find_min_cost_node(costs)
while node is not None: #모든 정점을 처리하면 알고리즘 종료
    cost = costs[node]
    neighbors = graph[node]
    for i in neighbors.keys(): #모든 이웃에 대해 반복
        new_cost = cost + neighbors[i]
        if costs[i] > new_cost: #만약 이 노드를 지나는 것이 더 싸다면
            costs[i] = new_cost #가격 갱신
            parents[i] = node #부모 갱신
    processed.append(node)
    node = find_min_cost_node(costs)

