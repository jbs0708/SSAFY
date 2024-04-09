import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def div(s, e):
    if s == e:
        return s
    g1 = div(s, (s+e) // 2)
    g2 = div((s+e)//2 + 1, e)
    return rsp(g1, g2)

def rsp(a, b):
    if list_[b] - list_[a] == 1 or list_[b] + 2 == list_[a]:
        return b
    else:
        return a


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    list_ = list(map(int, input().split()))
    print(f'#{tc} {div(0, N-1) + 1}')