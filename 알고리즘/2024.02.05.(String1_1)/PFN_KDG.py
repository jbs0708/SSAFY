for T in range(int(input())):
    X = input()
    Y = X[::-1]

    if X == Y:
        print(f"#{T + 1} 1")
    else:
        print(f"#{T + 1} 0")