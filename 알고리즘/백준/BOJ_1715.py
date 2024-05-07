import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')

N = int(input())
inp_list = []

for i in range(N):
    inp_list.append(int(input()))

inp_list.sort()

ans = 0
temp = 0
for p in inp_list:
    ans += p + temp
    temp = p

print(ans)