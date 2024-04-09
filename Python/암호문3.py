T = int(10)

for tc in range (1, T+1):
    N = int(input())
    str = input().split()
    M = int(input())
    order = input().split()

    for i in range(len(order)):
        if order[i] == 'I':
            x, y = int(order[i+1]), int(order[i+2])
            for j in range(y):
                str.insert(x + j, order[i+3+j])
        elif order[i] == 'A':
            y = int(order[i+1])
            for j in range(y):
                str.append(order[i+2+j])
        elif order[i] == 'D':
            x, y = int(order[i+1]), int(order[i+2])
            for j in range(y):
                str.pop(x + j)

    print(f"#{tc} ", end="")
    for i in range(10):
        print(f"{str[i]} ", end = "")
    print()

