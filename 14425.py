import sys

n, m = map(int, sys.stdin.readline.strip().split())
word_set = set([sys.stdin.readline.strip() for _ in range(n)])

cnt = 0
for _ in range(m):
    word = sys.stdin.readline.strip()
    if word in word_set:
        cnt += 1
        
print(cnt)