import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = 10

for tc in range(1, T+1):
    N = int(input())

    list_ = [list(input()) for _ in range(8)]

    cnt = 0

    for y in range(8):
        for x in range(8 - N + 1):
            found = True
            for n in range(N//2):
                if list_[y][x+n] != list_[y][x+(N-1)-n]:
                    found = False
                    break
            if found:
                cnt += 1

    for x in range(8):
        for y in range(8 - N + 1):
            found = True
            for n in range(N//2):
                if list_[y+n][x] != list_[y+(N-1)-n][x]:
                    found = False
                    break
            if found:
                cnt += 1

    print(f'#{tc} {cnt}')




