import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


def binary_search(key, l, r):
    start = 0
    end = N - 1
    while start <= end:
        if l == 2 or r == 2:
            return False
        mid = (start + end) // 2
        if list_[mid] == key:
            return True
        elif list_[mid] > key:
            end = mid - 1
            l += 1
            r = 0
        else:
            start = mid + 1
            r += 1
            l = 0
    return False


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    list_ = list(map(int, input().split()))
    list_.sort()
    m_list = list(map(int, input().split()))
    cnt = 0

    for key in m_list:
        l, r = 0, 0
        if key in list_:
            if binary_search(key, l, r):
                cnt += 1

    print(f'#{tc} {cnt}')