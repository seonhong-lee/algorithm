import sys

n = int(sys.stdin.readline().strip())
number_li = []

for i in range(n):
    input_number = int(sys.stdin.readline().strip())
    if input_number != 0:
        number_li.append(input_number)
    else:
        number_li.pop()

print(sum(number_li))
