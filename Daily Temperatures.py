
# step 1) 문제 이해하기
# 매일의 온도를 나타내는 int형 배열 temperatures가 주어진다. answer배열의 원소 answer[i]는 i번째 날의 온도보다 더 따듯해지기까지 며칠을
# 기다려야 하는지 나타낸다. 만약 더 따듯해지는 날이 없다면 answer[i] == 0이다. answer 배열을 반환하는 함수를 구현하시오.
# 제약 조건
# 1. 1 <= temperatures.length <= 10^5 => input size가 N 결국 빅오를 O(N)으로 해결해야하는 문제로 생각
# 2. 30 <= temperatures[i] <= 100 # 시간복잡도에는 큰 영향을 주지는 않음

# step 2) 접근 방법
# 2.1 직관적으로 생각하기
#   보통 완전탐색으로 시작
#   문제 상황을 단순화 하여 생각하기
#   문제 상황을 극한화 하여 생각하기
# 2.2 자료구조와 알고리즘 활용
#   (1) 믄제이해 에서 파악한 내용을 토대로 어떤 자료구조를 사용하는게 가장 적합한지 결정
#   대놓고 특정 자료구조와 알고리즘을 묻는 문젣 많은
#   자료구조에 따라 선택할 수 있는 알고리즘을 문제에 적용
# 2.3 메모리 사용
#   시간복잡도를 줄이기 위해 메모리를 사용하는 방법
#   대표적으로 해시테이블

# 완전 탐색으로 간다면 N^2으로가서 10^10으로 10^8을 초과해서 문제가 발생한다.
# 다른 방법은 없을까? 
# 단조로 증가한다면, ans는 [1, 1, 1, 1, ..., 0] 이런식으로 될 것이고
# 단조로 감소함다면, ans는 [0, 0, 0, 0, ..., 0] 이런식으로 될 것이다. 
# 단조로 증가하다가 단조로 감소한다면, ans는 [1, 1, 1, 1, 0, 0, 0, 0]이런식으로 될 것이다.
# 단조로 감소하다가 단조로 증가한다면, ans는 [7, 5, 3, 1, 1, 1,... ]이런식으로 될 것이다. 


# example1
# input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# output: [1, 1, 4, 2, 1, 1, 0, 0]
# example2
# input: temperatures = [30, 40, 50, 60]
# output: [1, 1, 1, 0]

# step 3) 코드 설계
# 간단하게 코드설계


# step 4) 코드 구현
def dailyTemperatures(temperatures):
    ans = [0] * len(temperatures)
    stack = []
    for cur_day, cur_temp in enumerate(temperatures):
        while stack and stack[-1][1] < cur_temp:
            prev_day, _ = stack.pop()
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))
    
    return ans

ans = dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
print(ans)