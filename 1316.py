import sys

n = int(sys.stdin.readline().strip())
str_li = [sys.stdin.readline().strip() for _ in range(n)]

def check_group_word(words):
    first_alpha = words[0]
    check_set = {first_alpha}
    for i in range(1, len(words)):
        if words[i] == words[i-1]:
            continue
        elif words[i] != words[i-1] and words[i] not in check_set:
            check_set.add(words[i])
        else:
            return False
    return True

answer_li = [check_group_word(i) for i in str_li]
print(sum(answer_li))