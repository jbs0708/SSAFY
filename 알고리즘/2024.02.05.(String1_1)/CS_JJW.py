T = int(input())

for test_case in range(1, T + 1):
    find_str = list(map(str, input()))
    whole_str = list(map(str, input()))
    length = len(find_str)
    cnt = 0
    check = 0
    for i in whole_str:
        if i == find_str[cnt]:
            cnt = cnt + 1
            if cnt == length:
                check = 1
                break
        else:
            cnt = 0
    print(f'#{test_case} {check}')