import math

NS = list(map(int, input().split()))
N = NS[0]
S = NS[1]

n_list = list(map(int, input().split()))

n_list.append(S)
n_list.sort()
max_ = 0

if N == 1:
    max_ = n_list[1] - n_list[0]
else:
    max_ = n_list[1] - n_list[0]
    for n in range(N):
        max_ = math.gcd(n_list[n + 1] - n_list[n], max_)

print(max_)
