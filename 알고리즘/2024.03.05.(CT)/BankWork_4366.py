import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    binary = list(input())
    ternary = list(input())

    b_list = []
    ans = 0

    for b in range(len(binary)):
        if binary[b] == '1':
            binary[b] = '0'
        else:
            binary[b] = '1'

        temp_b = ''
        for i in range(len(binary)):
            temp_b += binary[i]

        temp_b = int(temp_b, 2)
        b_list.append(temp_b)

        if binary[b] == '1':
            binary[b] = '0'
        else:
            binary[b] = '1'

    for t in range(len(ternary)):
        for i in range(2):
            if ternary[t] == '0':
                ternary[t] = '1'
            elif ternary[t] == '1':
                ternary[t] = '2'
            elif ternary[t] == '2':
                ternary[t] = '0'

            temp_t = ''
            for e in range(len(ternary)):
                temp_t += ternary[e]

            temp_t = int(temp_t, 3)
            if temp_t in b_list:
                ans = temp_t
                break

        if ans:
            break

        if ternary[t] == '0':
            ternary[t] = '1'
        elif ternary[t] == '1':
            ternary[t] = '2'
        elif ternary[t] == '2':
            ternary[t] = '0'

    print(f'#{tc} {ans}')
