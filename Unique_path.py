# 이 로봇은 m x n grid(격자)위에 존재한다. 로봇은 처음에 좌측 상단 모서리 grid[0][0]에 위치해 있다. 로봇은 우측 하단 모서리
# grid[m-1][n-1]로 이동하려고 한다. 로봇은 한 번에 오른쪽이나 아래쪽으로만 움직일 수 있다.
# 두 정수 m과 n이 주어졌을 때, 로봇이 우측 하단 모서리에 도달할 수 있는 가능한 unique paths의 수를 반환하라.
# 테스트 케이스는 답이 2*10^9 이하가 되도록 생성된다.

# 제약조건
# 1. 1 <= m,n <= 100

# input: m=3, n=7
# output: 28
# input: m=3, n=2
# output: 3

def dfs(r, c): 
    if r==2 and c==6:
        return 1
    unique_paths = 0
    if r+1 < 3:
        unique_paths += dfs(r+1, c)
    if c+1 < 7:
        unique_paths += dfs(r, c+1)
    return unique_paths

def dfs(r, c):
    if r==0 and c==0:
        return 1
    unique_paths = 0
    if r-1 >= 0:
        unique_paths += dfs(r-1, c)
    if c-1 >= 0:
        unique_paths += dfs(r, c-1)
        
    return unique_paths

memo = {}
def dfs(r, c):
    if r==0 and c==0:
        memo[(r, c)] = 1
        return memo[(r, c)]
    if (r, c) not in memo:
        if r-1 >= 0:
            unique_paths += dfs(r-1, c)
        if c-1 >= 0:
            unique_paths += dfs(r, c-1)
        memo[(r, c)] = unique_paths
        
    return memo[(r, c)]

def uniquePaths(m, n):
    memo = [[-1]*n for _ in range(m)]
    def dfs(r, c):
        if r==0 and c==0:
            memo[r][c] = 1
            return memo[r][c]
        unique_paths = 0
        if memo[r][c] == -1:
            if r-1 >= 0:
                unique_paths += dfs(r-1, c)
            if c-1 >= 0:
                unique_paths += dfs(r, c-1)
            memo[r][c] = unique_paths
        return memo[r][c]
    return dfs(m-1, n-1)

uniquePaths(3, 7)

def uniquePaths(m, n):
    memo = [[-1]*n for _ in range(m)]
    for r in range(m):
        memo[r][0] = 1
    for c in range(n):
        memo[0][c] = 1
    
    for r in range(1, m):
        for c in range(1, n):
            memo[r][c] = memo[r-1][c] + memo[r][c-1]
            
    return memo[m-1][n-1]

uniquePaths(3, 7)


    