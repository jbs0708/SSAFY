import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')

T = int(input())
list_ = [2, 3, 5, 7, 11]

for tc in range(1, T+1):
    prime_list = []
    N = int(input())
    for p in list_:
        cnt = 0
        while True:
            if N % p != 0:
                break
            else:
                N //= p
                cnt += 1
        prime_list.append(cnt)

    print(f'#{tc} ',end='')
    for i in prime_list:
        print(f'{i} ',end='')
    print()