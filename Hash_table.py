# 해시테이블(Hash Table)
# 필수적으로 나오고 핵심적인 자료구조. 
# 어느 상황에서 사용하는 것이 중요하다.
# Hash Table은 
# 1. Array List based (open addressing)
# 2. Find key O(1)
# 3. Array list + linked list (separate chaining)
# 파이썬에서는 hash table로 딕셔너리를 만들었음.
# hash table은 충돌이 일어난다. 충돌이 일어났을 때, 이를 해결할 수 있는 것 위의 ()가 해결

# Direct-address Table은 hash table과 반대되는 개념, key 값이 index가 된다. 
# 하지만 이러한 구조는 불필요한 공간을 낭비하고 key값으로 문자열이 올 수 없다.
# 그래서 직접 주소화 방법은 (key, value) 데이터 쌍을 저장하기 위한 방법으로는 잘 맞지가 않는다. 그래서 Hash Table을 사용하는 것.

# 모든 데이터에는 key값은 무조건 존재해야 하며, 중복되는 key값이 있어서는 안된다. 
# Collision이 발생했을 때, 옆으로 한 칸, 몇 칸, 혹은 rehashing을 하냐에 따라 여러가지 open addressing 방법등이 존재한다. 
# 가장 간단한 방법이 다음 index에 저장하는 것.
# hash table의 시간복잡도는 저장, 삭제, 검색 모두 기본적으로 O(1)이다. 
# 파이썬의 딕셔너리는 hash table로 구현되어 있다.

# 핵심은 in 연산자
# 딕셔너리는 in 연산자와 결합했을 때, 힘을 발휘.
# 만약 key가 존재하면, True를 반환하고 존재하지 않으면, False를 반환.
# 이는 기존 리스트에서는 O(n)이 걸리는 시간 복잡도를 O(1)으로 줄여주는 과정이며 핵심이다.
# 이는 메모리를 사용해서 시간복잡도를 줄여주는 상황을 보여준다. 

nums = [4, 1, 9, 5, 7, 3, 16]
target = 14

def hash_table(nums, target):
    hash_di = {}
    for i in nums:
        hash_di[i] = True
    for i in nums:
        temp_value = target - i
        if temp_value in hash_di and temp_value != i:
            return True

    return False

print(hash_table(nums, target))