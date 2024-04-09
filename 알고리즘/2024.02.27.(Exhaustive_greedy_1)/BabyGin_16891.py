import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


def check(player, card, p_num):
    global winner

    player[card] += 1
    if player[card] == 3:
        winner = p_num
        return
    else:
        for n in range(max(card-2, 0), card+1):
            if player[n] > 0 and player[n + 1] > 0 and player[n + 2] > 0:
                winner = p_num
                return


T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    winner = 0

    p1 = [0 for _ in range(12)]
    p2 = [0 for _ in range(12)]

    for i in range(12):
        if i % 2 == 0:
            check(p1, cards[i], 1)
            if winner:
                break
        else:
            check(p2, cards[i], 2)
            if winner:
                break

    print(f'#{tc} {winner}')

