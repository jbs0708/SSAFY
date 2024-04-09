for T in range(int(input())):
    N = int(input())
    l = list(map(int, input().split()))
    print(f'#{T + 1}', sorted(l)[N // 2])