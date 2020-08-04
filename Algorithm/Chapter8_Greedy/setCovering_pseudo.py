'''
집합 커버링 문제

나는 라디오 쇼를 진행하고 있으며, 미국 50개 주에 있는 모든 사람에게 라디오 쇼를 들려주고 싶다. 
하나의 방송국이 커버하는 지역이 한정되어 있기 대문에 전국에 흩어져 있는 몇 개의 라디오 방송국을 방문해서 라디오 쇼를 진행해야 한다.
전국의 모든 사람들이 최소한 한 번은 쇼를 들을 수 있도록 어떤 방송국을 방문해야 할지, 최대한 적은 수의 방송국을 선택한다.
'''

# 문제 단순화를 위해 일부 주 만 사용
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# 방송국이 커버하는 지역 목록
# key: 방송국 이름 val: 그 방송국의 방송을 들을 수 있는 주 목록
stations = {}
stations["knoe"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa","id","mt"])
stations["kthree"] = set(["or","nv","ca"])
stations["kfour"] = set(["nv","ut"])
stations["kfive"] = set(["ca", "az"])

# 방문할 방송국 목록 저장
final_stations = set()

while states_needed:
    # 아직 방송이 되지 않은 주 중에서 가장 많은 주를 커버하는 방송국
    best_station = None

    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states  # 아직 방송되지 않은 주 중에서 해당 방송국이 커버하는 주의 집합
        if len(covered) > len(states_covered): # 이 방송국이 현재 best_station보다 더 많은 주를 커버할 경우
            best_station = station # 그 방송국을 best_station으로 등록
            states_covered = covered # 방송된 주 목록

    final_stations.add(best_station) # 최후의 best_station을 최적의 방송국으로 등록
    states_needed -= states_covered # 해당 방송국에서 커버하는 주 제외

# states_needed가 빌 때 까지 반복
print(final_stations)