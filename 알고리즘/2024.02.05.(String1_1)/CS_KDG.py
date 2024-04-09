for T in range(int(input())):
    X = input()
    Y = input()

    if X in Y:
        print(f"#{T + 1} 1")
    else:
        print(f"#{T + 1} 0")