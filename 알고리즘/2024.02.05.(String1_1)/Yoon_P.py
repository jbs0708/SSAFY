import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = 10

for tc in range(1, T+1):

    N = int(input())
    count_ = 0
    list_ = [list(map(str, (input().split()))) for _ in range(8)]
    for i in range(8):
        for j in range(8):

            P = list_[i][j]
            for i in range(0, 8 - N):
                if N == 2:
                    if list_[i][j] == list_[i][j + 1]:
                        count_ += 1
                if N == 3:
                    if list_[i][j] == list_[i][j + 2]:
                        count_ += 1
                if N == 4:
                    if list_[i][j] == list_[i][j + 3] and list_[i][j + 1] == list_[i][j + 2]:
                        count_ += 1
                if N == 5:
                    if list_[i][j] == list_[i][j + 4] and list_[i][j + 1] == list_[i][j + 3]:
                        count_ += 1
                if N == 6:
                    if list_[i][j] == list_[i][j + 5] and list_[i][j + 1] == list_[i][j + 4] and list_[i][j + 2] == \
                            list_[i][j + 3]:
                        count_ += 1
                if N == 7:
                    if list_[i][j] == list_[i][j + 6] and list_[i][j + 1] == list_[i][j + 5] and list_[i][j + 2] == \
                            list_[i][j + 4]:
                        count_ += 1
                if N == 8:
                    if list_[i][j] == list_[i][j + 7] and list_[i][j + 1] == list_[i][j + 6] and list_[i][j + 2] == \
                            list_[i][j + 5] and list_[i][j + 3] == list_[i][j + 4]:
                        count_ += 1
            for j in range(0, 8 - N):
                if N == 2:
                    if list_[i][j] == list_[i + 1][j]:
                        count_ += 1
                if N == 3:
                    if list_[i][j] == list_[i + 2][j]:
                        count_ += 1
                if N == 4:
                    if list_[i][j] == list_[i + 3][j] and list_[i + 1][j] == list_[i + 2][j]:
                        count_ += 1
                if N == 5:
                    if list_[i][j] == list_[i + 4][j] and list_[i + 1][j] == list_[i + 3][j]:
                        count_ += 1
                if N == 6:
                    if list_[i][j] == list_[i + 5][j] and list_[i + 1][j] == list_[i + 4][j] and list_[i + 2][j] == \
                            list_[i + 3][j]:
                        count_ += 1
                if N == 7:
                    if list_[i][j] == list_[i + 6][j] and list_[i + 1][j] == list_[i + 5][j] and list_[i + 2][j] == \
                            list_[i + 4][j]:
                        count_ += 1
                if N == 8:
                    if list_[i][j] == list_[i + 7][j] and list_[i + 1][j] == list_[i + 6][j] and list_[i + 2][j] == \
                            list_[i + 5][j] and list_[i + 3][j] == list_[i + 4][j]:
                        count_ += 1

            print(count_)