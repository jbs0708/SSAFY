import sys

n, q = map(int, input().split())
cars = list(map(int, input().split()))
cars.sort()
dict_ = {}

cnt = 1
for i in cars:
    dict_[i] = cnt
    cnt += 1

for i in range(q):
    temp = int(input())
    if dict_.get(temp, False):
        print((dict_[temp]-1) * (n - dict_[temp]))
    else:
        print(0)