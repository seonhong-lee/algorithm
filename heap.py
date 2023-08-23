import heapq

# min heap 과정
min_heap = [5, 3, 9, 4, 1, 2, 6]

heapq.heapify(min_heap)
print(min_heap)

heapq.heappop(min_heap)
print(min_heap)

heapq.heappush(min_heap, 0)
print(min_heap)

# max heap 과정
max_heap = [5, 3, 9, 4, 1, 2, 6]
heapq._heapify_max(max_heap)
value = heapq._heappop_max(max_heap)
print(value)
# 이렇게 할 수도 있지만, min_heap을 이용해서 max heap
# 구조를 만들 수 있다.


max_heap = [5, 3, 9, 4, 1, 2, 6]
max_heap = [i * -1 for i in max_heap]
heapq.heapify(max_heap)
weight = heapq.heappop(max_heap)
value = -1 * weight
print(value)

# 추후에 다익스트라 알고리즘을 구현하기 위해서는
# 우선순위 큐가 필요하다. 그때는 그냥 heap을 이용하면 된다.
