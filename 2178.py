import sys
from collections import deque


short_path = 0
n, m = int(sys.stdin.readline().split())
map_li = [sys.stdin.readline().split() for _ in range(n)]

visited = [[False]*m for _ in range(n)]
visited[0][0] = True

queue = deque()
queue.append((0, 0, 1))

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

while queue:
    cur_r, cur_c, cur_length = queue.popleft()
    
    if cur_r == n-1 and cur_c == m-1:
        short_path = cur_length
        break    
    
    for i in range(4):
        next_r, next_c = cur_r + dr[i], cur_c + dc[i]
        
        if next_r >= 0 and next_r < n and next_c >= 0 and next_c < m:
            if not visited[next_r][next_c] and map_li[next_r][next_c] != 0:
                visited[next_r][next_c] = True
                queue.append((next_r, next_c, cur_length+1))
                
print(short_path)
    