import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


def func(start, cnt):
    global max_

    # 변경횟수를 다쓴 상태라면
    if cnt == 0:
        # 현재 카드의 상태 sum_
        sum_ = ''
        # 순서대로 정렬하고
        for s in str_list:
            sum_ += s
        # 정렬된 숫자를 정수형으로 변환하여 현재 최종값과 비교하여 갱신
        ans = max(ans, int(sum_))
        return

    ## 완탐 ##
    # for[시작점 ~ 끝점-1]
    #   for[시작점+1 ~ 끝점]
    for i in range(start, len(str_input)-1):
        for j in range(i+1, len(str_input)):
            # 전부 스위칭해보고 재귀함수 호출
            str_list[i], str_list[j] = str_list[j], str_list[i]
            func(i, cnt-1)
            # 다른 경우의 수도 확인하기위해 다시 원복
            str_list[i], str_list[j] = str_list[j], str_list[i]


T = int(input())

for tc in range(1, T+1):
    str_input, N = input().split()
    N = int(N)

    # 변경 횟수 줄이기
    if len(str_input) < N and N % 2 == 0:
        N = len(str_input)

    # 자릿수 조합을 편하게 하기 위해 string으로 진행
    str_list = list(str_input)
    # 최종 결과값 ans
    max_ = 0
    func(0, N)
    print(f'#{tc} {max_}')

