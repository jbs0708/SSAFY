import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    A, B = map(str, input().split())


    max_ = 0
    a = 0
    while a < len(A):
        cnt = 0
        if A[a:a+len(B)] == B:
            max_ += 1
            a += len(B)
        else:
            max_ += 1
            a += 1

    print(f'#{tc} {max_}')