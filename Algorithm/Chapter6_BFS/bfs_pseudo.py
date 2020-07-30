from collections import deque

'''
그래프 연결 관계 표현
'''
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuji", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["tom", "jonny"]
graph["anuji"] = []
graph["tom"] = []
graph["jonny"] = []
graph["peggy"] = []

def bfs_test(name):
    searched = [] #이미 확인한 사람인지 추적하기 위해.
    '''
    탐색 목록
    '''
    search_queue = deque()
    search_queue += graph[name] #name의 모든 이웃 목록을 탐색 큐에 추가

    while search_queue:
        person = search_queue.popleft() #popleft: 가장 앞쪽부터 꺼냄.
        if not person in searched: #이전에 확인하지 않은 사람만 탐색
            if target_person(person):
                print(person+" is a Mango seller!")
                return True
            else:
                search_queue += graph[person] #person의 모든 이웃을 탐색 목록에 추가.
                searched.append(person)
    return False #타겟이 없을 때.

'''
그 사람이 타겟인지 확인하는 예시 함수.
타겟은 이름이 m자로 끝난다.
'''
def target_person(name):
    return name[-1] == 'm'

if __name__ == '__main__':
    bfs_test("you")