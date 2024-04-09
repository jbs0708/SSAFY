import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


def card_set():
    global cards
    new_cards = []

    over1 = cards[:N-rate]
    over2 = cards[N-rate:]
    overhands = over2 + over1

    if N % 2 == 1:
        perf1 = overhands[:N//2 + 1]
        perf2 = overhands[N//2 + 1:]
        for i in range(N):
            if i % 2 == 0:
                new_cards.append(perf1[i // 2])
            else:
                new_cards.append(perf2[i // 2])
    else:
        perf1 = overhands[:N//2]
        perf2 = overhands[N//2:]
        for i in range(N):
            if i % 2 == 0:
                new_cards.append(perf1[i // 2])
            else:
                new_cards.append(perf2[i // 2])

    cards = new_cards
    return


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cards = [i for i in range(1, N+1)]
    rate = int(N * 0.37)

    for m in range(M):
        card_set()

    print(f'#{tc} ', end='')
    for q in cards:
        print(q, end=' ')
    print()
