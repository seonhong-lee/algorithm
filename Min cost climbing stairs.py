# 계단을 올라가고 있다. 한 번 올라갈 때마다 1step 또는 2step을 올라갈 수 있다. 문제에서 정수형 배열 cost가 주어지는데,
# cost[i]는 i번 째 계단을 밟았을 때 지불해야 하는 비용이다.

# 처음 시작은 index 0 또는 index 1 중 한 곳에서 시작할 수 있다.

# 이 계단의 꼭대기에 도착하기 위해 지불해야하는 비용의 최솟값을 반환하라.
# 제약조건
# 1. 2 <= cost.length <= 1000
# 2. 0 <= cost[i] <= 999

# input: cost = [10, 15, 20]
# output: 115

# input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# output: 6
import sys
sys.setrecursionlimit(10**8)


cost = [10, 15, 20, 17, 1]
memo = {}
def dp1(n):
    if n==0 or n==1:
        return 0
    if n not in memo:
        memo[n] = min(dp1(n-1) +cost[n-1], dp1(n-2) + cost[n-2])
        
    return memo[n]
print(dp1(5))
print(memo)


cost1 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
def dp2(n):
    memo = [-1]*n
    memo[0] = 0
    memo[1] = 0
    
    for i in range(2, n):
        memo[i] = min(memo[i-1] + cost1[i-1], memo[i-2] + cost1[i-2])
    print(memo)
    return memo[n-1]

print(dp2(len(cost1) + 1))

