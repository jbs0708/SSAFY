N = int(input())
list_ = list(map(int, input().split()))
list_.append(1000000001)
list_.insert(0,1)

if N <= 3:
    print('YES')
    for i in range(1, N+1):
        print(f'{i} {i}')
else:
    repair_list = []
    i = 1
    while i <= N:
        if len(repair_list) > 4:
            break
        if list_[i] > list_[i+1]:
            repair_list.append(i)
            i += 1
        elif list_[i] < list_[i-1]:
            repair_list.append(i-1)
        i += 1

    print(repair_list)

    if len(repair_list) <= 3:
        fix_list = []
        for i in repair_list:
            list_[i] = list_[i-1]
            fix_list.append(i)
            fix_list.append(list_[i-1])

        print('YES')
        for i in range(len(repair_list)):
            for j in range(2):
                print(fix_list[(i*2)+j], end=' ')
            print()
    else:
        print('NO')


    # cnt = 0
    # fix_list = []
    # i = 1
    # while i <= N:
    #     if cnt > 4:
    #         break
    #     if list_[i] > list_[i+1]:
    #         list_[i] = list_[i+1]
    #         cnt += 1
    #         fix_list.append(i)
    #         fix_list.append(list_[i-1])
    #         i = 0
    #     if list_[i] < list_[i-1]:
    #         list_[i] = list_[i-1]
    #         cnt += 1
    #         fix_list.append(i)
    #         fix_list.append(list_[i-1])
    #         i = 0
    #     i += 1
    # if cnt <= 3:
    #     print('YES')
    #     for i in range(cnt):
    #         for j in range(2):
    #             print(fix_list[(i*2)+j], end=' ')
    #         print()
    # else:
    #     print('NO')