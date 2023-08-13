# 0번방부터 n-1번방까지 총 n개의 방이 있다. 0번 방을 제외한 모든 방은 잠겨있다. 우리의 목표는 모든 방에 visit하는 것이다.
# 하지만 잠겨져 있는 방은 key가 없으면 visit할 수 없다. 각 방에 방문할 때, 별개의 열쇠뭉치(a set of distint keys)를 찾을 수도 있다.
# 각각의 열쇠에는 number가 쓰여져 있고, 해당 번호에 해당하는 방을 잠근 해제할 수 있다. 열쇠뭉치는 모두 가져갈 수 있고, 언제든
# 방문을 열기 위해 사용할 수 있다.

# 문제에서 rooms 배열이 주어지고, rooms[i]는 해당 방에서 얻을 수 있는 열쇠뭉치 목록을 표현한다.
# 모든 방을 visit할 수 있다면, True, 그렇지 않으면 False를 반환하라.

# n == rooms.length
# 2 <= n <= 1000
# 0 <= rooms[i].length <= 1000
# 1 <= sum(room[i].length) <= 3000
# 0 <= rooms[i][j] < n

# BFS는 예약을 하면서 visit을 한다. queue에 올릴때, 중복되는 경우가 발생할 수 있기 때문.
from collections import deque


def canVisitAllRooms(rooms):
    visited = [] # 5번방 방문 안했네? => False // True
    
    # v에 연결되어 있는 모든 vertex 방문 예정.
    def dfs(v):
        visited.append(v)
        for next_v in rooms[v]:
            # 해시 셋 or 헤세 테이블로 시간 복잡도를 향상 시킬 수 있다. 
            if next_v not in visited:
                dfs(next_v)
    
    def bfs(v):
        visited.append(v)
        queue = deque()
        queue.append(v)
        
        while queue:
            cur_v = queue.popleft()
            for next_v in rooms[cur_v]:
                if next_v not in visited:
                    visited.append(next_v)
                    queue.append(next_v)
                    
        return visited
        
    
    # dfs(0)
    bfs(0)
    if len(visited) == len(rooms):
        return True
    else: return False

rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
print(canVisitAllRooms(rooms))