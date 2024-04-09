N = int(input())
list_ = [0] * N

if N == 1:
    print('YES')
    print('1')
    print('1')
elif N == 2:
    print('YES')
    print('1 2')
    print('1 2')
else:
    if N % 2 == 1:
        temp = N//2
        seq_list = [temp+1]
        for i in range(1, N+1):
            list_[temp] = i
            if i % 2 == 1:
                temp += i
                seq_list.append(temp+1)
            else:
                temp -= i
                seq_list.append(temp+1)
        seq_list.pop()

        print('YES')
        print(*list_)
        print(*seq_list)
    else:
        temp = N//2 - 1
        seq_list = [temp+1]
        for i in range(1, N+1):
            list_[temp] = i
            if i % 2 == 1:
                temp += i
                seq_list.append(temp + 1)
            else:
                temp -= i
                seq_list.append(temp + 1)
        seq_list.pop()
        print('YES')
        print(*list_)
        print(*seq_list)