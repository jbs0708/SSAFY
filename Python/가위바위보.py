def determine_winner(a, b):
    if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
        return "A"
    else:
        return "B"

# 사용자로부터 A와 B가 무엇을 냈는지 입력 받음
a, b = map(int, input().split())

result = determine_winner(a, b)

print(result)