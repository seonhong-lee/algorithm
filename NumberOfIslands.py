# grid는 "1"(land) 과 "0"(water)으로 이루어진 지도를 표현하는 m x n 이차원배열이다.
# 이 지도에 표시된 섬들의 총 갯수를 반환하시오.
# 섬이란 수평과 수직으로 땅이 연결되어 있고 주변은 물로 둘러쌓여있는 것을 말한다.
# 또한, grid의 네개의 가장자리는 모두 물로 둘러쌓여 있다고 가정하고 문제를 해결하라.

# m == grid.length
# n == grid[i].length
# 1<= m,n <= 300
# grid[i][j] is '0' or '1'

from collections import deque

def numberOfIsland(grid):
    cnt_of_island = 0
    
    row = len(grid)
    col = len(grid[0])
    
    visited = [[False]*col for _ in range(row)]
    
    def bfs(r, c):
        visited[r][c] = True
        queue = deque()
        queue.append((r, c))
        
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        
        while queue:
            cur_row, cur_col = queue.popleft()
            
            for i in range(4):
                next_row, next_col = cur_row+dr[i], cur_col+dc[i]
                
                if next_row >= 0 and next_row < row and next_col >= 0 and next_col < col: 
                    if grid[next_row][next_col] != '0' and not visited[next_row][next_col]:
                        visited[next_row][next_col] = True
                        queue.append((next_row, next_col))
        
    
    for r in range(row):
        for c in range(col):
            if grid[r][c] == '1' and not visited[r][c]:
                bfs(r, c)
                cnt_of_island += 1
                

    return cnt_of_island

grid_1 = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
]

grid_2 = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1'],
]

print(numberOfIsland(grid_1))
print(numberOfIsland(grid_2))
























def numberOfIsland_2(grid):
    cnt_of_island = 0
    
    row = len(grid)
    col = len(grid[0])
    
    visited = [[False]*col for _ in range(row)]

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        visited[r][c] = True
        
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        
        while queue:
            cur_r, cur_c = queue.popleft()
            for i in range(4):
                next_r, next_c = cur_r+dr[i], cur_c+dc[i]
                
                if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
                    if  grid[next_r][next_c] != '0' and not visited[next_r][next_c]:
                        queue.append((next_r, next_c))
                        visited[next_r][next_c] = True             

    for r in range(row):
        for c in range(col):
            if grid[r][c] != '0' and not visited[r][c]:
                bfs(r, c)
                cnt_of_island += 1
        
    return cnt_of_island        


grid_1 = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
]

grid_2 = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1'],
]

print(numberOfIsland_2(grid_1))
print(numberOfIsland_2(grid_2))






def numberOfIsland_3(grid):
    cnt_of_island = 0
    
    len_row = len(grid)
    len_col = len(grid[0])
    
    visited = [[False]*len_col for _ in range(len_row)]
    
    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        
        visited[r][c] = True
    
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        
        while queue:
            cur_r, cur_c = queue.popleft()
            
            for i in range(4):
                next_r, next_c = cur_r + dr[i], cur_c + dc[i]
                
                if next_r >= 0 and next_r < len_row and next_c >= 0 and next_c < len_col:
                    if grid[next_r][next_c] != '0' and not visited[next_r][next_c]:
                        visited[next_r][next_c] = True
                        queue.append((next_r, next_c))
    
    for r in range(len_row):
        for c in range(len_col):
            if grid[r][c] != "0" and not visited[r][c]:
                bfs(r, c)
                cnt_of_island += 1
                
    return cnt_of_island

grid_1 = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
]

grid_2 = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1'],
]

print(numberOfIsland_3(grid_1))
print(numberOfIsland_3(grid_2))