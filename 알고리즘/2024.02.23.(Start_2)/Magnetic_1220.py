import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

results = []

for t in range(1, 11):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    count = 0

    for i in range(N):

        matrix = list(map(int, input().split()))
        for j in range(N):
            arr[i][j] = matrix[j]

    for i in range(N):
        check = True
        for j in range(N):
            if check and arr[j][i] == 1:
                check = False
            elif not check and arr[j][i] == 2:
                count += 1
                check = True

    results.append(count)

for idx, result in enumerate(results, start=1):
    print(f"#{idx} {result}")