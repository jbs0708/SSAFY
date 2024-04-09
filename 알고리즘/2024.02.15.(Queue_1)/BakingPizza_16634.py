import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 치즈 대기열
    cheese = deque(map(int, input().split()))

    # 화덕
    fire_pit = deque()

    # 마지막 남은 치즈의 번호
    last_idx = 0
    # 각 치즈들 번호 매기기용
    idx = 1
    while True:
        # 대기중인 치즈가 있다 and 화덕안에 자리가 빈다면
        while cheese and len(fire_pit) != N:
            # 화덕에 넣고 넘버링 [치즈양, 번호]
            fire_pit.append([cheese.popleft(), idx])
            # 번호 += 1
            idx += 1

        # 화덕에 뭔가 있다면
        if fire_pit:
            # 화덕에서 하나 꺼내기
            nextCheese = fire_pit.popleft()
            # 이 때, 얘가 마지막 생존치즈일 수 있으니 번호 저장
            last_idx = nextCheese[1]

            # 나누기 2 했을 때 0보다 큰지 확인
            if nextCheese[0] // 2 > 0:
                # 크다면 나누기 2하고 다시 화덕행
                fire_pit.append([nextCheese[0]//2, nextCheese[1]])
        # 화덕이 빈다면
        else:
            break

    print(f'#{tc} {last_idx}')




