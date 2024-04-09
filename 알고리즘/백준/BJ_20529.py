import sys


sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    student = list(map(str, input().split()))
    distance = 9999999

    # 비둘기집 원리
    if N > 32:
        print(0)
    else:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if i == k or i == j or j == k:
                        continue
                    temp = 0
                    for char in range(4):
                        if student[i][char] != student[j][char]:
                            temp += 1
                        if student[k][char] != student[j][char]:
                            temp += 1
                        if student[k][char] != student[i][char]:
                            temp += 1

                    distance = min(temp, distance)
        print(distance)

