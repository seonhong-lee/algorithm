import sys

n = int(sys.stdin.readline().strip())
words_li = [sys.stdin.readline().strip() for _ in range(n)]

for word in words_li:
    if len(word) == 1:
        print(word[0] + word[0])
    else:
        print(word[0] + word[-1])