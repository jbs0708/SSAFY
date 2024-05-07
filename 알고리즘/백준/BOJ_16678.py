
import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')


N = int(input())
inp_list = []

for i in range(N):
    inp_list.append(int(input()))

inp_list.sort()

num = 1
ans = 0
for p in inp_list:
    if p == num:
        num += 1
    elif p < num:
        continue
    else:
        ans += (p-num)
        num += 1

print(ans)
