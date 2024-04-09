turncnt = [
    [3,1,3,2],
    [2,3,1,3],
    [1,2,3,3],
    [3,3,2,1]
]

nextdir = [
    [2,3,2,1],
    [0,3,2,3],
    [0,3,1,1],
    [0,0,2,1]
]


T = int(input())

for t in range(T):
    N = int(input())

    MAP = []
    target = []

    for i in range(N):
        row = list(map(int,input().split()))
        MAP.append(row)
        for j in range(N):
            col = row[j]
            if col > 0 :
                target.append((col,i,j))


    target.sort()
    max_ = 1
    dir = 1

    y = target[0][1]
    x = target[0][2]

    for i in range(1, len(target)):
        ny = target[i][1]
        nx = target[i][2]

        # 좌상
        if ny < y and nx < x:
            max_ += turncnt[dir][0]
            dir = nextdir[dir][0]

        if ny < y and nx > x:
            max_ += turncnt[dir][1]
            dir = nextdir[dir][1]

        if ny > y and nx < x:
            max_ += turncnt[dir][2]
            dir = nextdir[dir][2]

        if ny > y and nx > x:
            max_ += turncnt[dir][3]
            dir = nextdir[dir][3]

        y = ny
        x = nx




    print(f'#{t+1} {max_}')