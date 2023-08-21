# 계단을 올라가고 있다. 이 계단의 꼭대기에 도착하려면 n개의 steps만큼 올라가야 한다.
# 한 번 올라갈 때마다 1 step 또는 2 steps 올라갈 수 있다. 꼭대기에 도달하는 방법의 개수는 총
# 몇 가지 인가?

# 제약 조건
# 1 <= n <= 45

# input: n = 2
# output: 2

# 1. 1 step + 1 step
# 2. 2 step

# input: n = 3
# output: 3
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 step
# 3. 2 step + 1 step

# 5층까지만 해도 어려운 문제가 된다. 
# 이렇게 크고 복잡한 문제를 하위문제로 나눠서.

# Top down 방식
# memorization
memo = {}
def cs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n not in memo:
        memo[n] = cs(n-1) + cs(n-2)
    
    return memo[n]

# Bottom up 방식
# dp table or tabulation
memo_1 = {}
def cs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    for i in range(3, n+1):
        memo_1[i] = memo_1[i-1] + memo_1[i-2] 
        
    return memo_1[n]

memo = {1: 1,
     2: 2,
     }
