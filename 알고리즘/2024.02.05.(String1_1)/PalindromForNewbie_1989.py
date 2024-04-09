import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    input_str = input()
    N = len(input_str)

    found = True
    for n in range(N//2):
        if input_str[n] != input_str[(N - 1) - n]:
            found = False
            break

    if found:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')