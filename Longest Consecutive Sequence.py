nums_1 = [100, 4, 200, 1, 3, 2, 201, 204]
nums_2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

def LCS(num_li):
    num_li.sort() # nlog(n)

    max_cnt = 0
    cnt = 1
    current_num = num_li[0]

    for num in num_li[1:]:
        if num == current_num+1:
            current_num = num
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            current_num = num
            max_cnt = max(max_cnt, cnt)
            cnt = 1

    return max_cnt

print(LCS(nums_1))
print(LCS(nums_2))

def hash_LCS(num_li):
    hash_di = {}
    max_cnt = 1
    for i in num_li:
        hash_di[i] = True
    for num in num_li:
        if num-1 not in hash_di:
            cnt = 1
            temp_value = num + 1
            while temp_value in hash_di:
                temp_value += 1
                cnt += 1
            max_cnt = max(max_cnt, cnt)
    return max_cnt

print(hash_LCS(nums_1))
print(hash_LCS(nums_2))