# n x n binary matrix인 grid가 주어졌을 때, 출발지에서 목적지까지 도착하는 가장빠른
# 경로의 길이를 반환하시오. 만약 경로가 없다면 -1을 반환하시오.

# 출발지: top-left cell
# 목적지: bottom-right cell

#- 값이 0인 cell만 지나갈 수 있다.
#- cell끼리는 8가지 방향으로만 연결되어 있다. (edge와 corner 방향으로 총 8가지이다.)
#- 연결된 cell을 통해서만 지나갈 수 있다.

# 제약 조건
# n == grid.length
# n == grid[i].legnth 
# 1 <= n <= 100
# grid[i][j] is 0 or 1

from collections import deque

grid_1 = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0]
]
# output: 4

grid_2 = [
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 0]
]
# output: -1



def SPBM(grid):
    cnt_of_short_path = -1
    matrix_len = len(grid)
    
    if grid[0][0] != 0 or grid[matrix_len-1][matrix_len-1] != 0:
        return cnt_of_short_path
    
    visited = [[False]*matrix_len for _ in range(matrix_len)]
    

    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True
    
    dr = [0, 0, 1, -1, 1, 1, -1, -1]
    dc = [-1, 1, 0, 0, 1, -1, 1, -1]
    
    while queue:
        cur_r, cur_c, cur_length = queue.popleft()
        if cur_r == matrix_len-1 and cur_c == matrix_len-1:
            cnt_of_short_path = cur_length
            break
        
        for i in range(8):
            next_r, next_c = cur_r + dr[i], cur_c + dc[i]
            if next_r >= 0 and next_r < matrix_len and next_c >= 0 and next_c < matrix_len:
                if grid[next_r][next_c] != 1 and not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    queue.append((next_r, next_c, cur_length + 1))
    
    return cnt_of_short_path



print(SPBM(grid_1))
print(SPBM(grid_2))


def SPBM2(grid):
    matrix_len = len(grid)
    cnt_shortest_path = -1
    
    if grid[0][0] == 1 or grid[matrix_len-1][matrix_len-1] == 1:
        return cnt_shortest_path
    
    visited = [[False]*matrix_len for _ in range(matrix_len)]
    visited[0][0] = True
    
    queue = deque()
    queue.append((0, 0, 1))
    
    dr = [0, 0, 1, -1, 1, 1, -1, -1] 
    dc = [1, -1, 0, 0, 1, -1, 1, -1]
    
    while queue:
        cur_r, cur_c, cur_length = queue.popleft()
        if cur_r == matrix_len-1 and cur_c == matrix_len-1:
            cnt_shortest_path = cur_length
            break
        
        for i in range(8):
            next_r, next_c = cur_r + dr[i], cur_c + dc[i]
            if next_r >= 0 and next_r < matrix_len and next_c >= 0 and next_c < matrix_len:
                if not visited[next_r][next_c] and grid[next_r][next_c] != 1:
                    visited[next_r][next_c] = True
                    queue.append((next_r, next_c, cur_length+1))
    
    return cnt_shortest_path

print(SPBM2(grid_1))
print(SPBM2(grid_2))