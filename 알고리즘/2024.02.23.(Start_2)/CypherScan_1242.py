import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 각 줄에 대해 헥사코드의 중복을 제외하여 리스트 생성
    matrix = set(input().strip() for _ in range(N))
    # '0'으로만 이루어진 줄을 제거하기 위해 정렬 후 가장 앞 원소 제거
    matrix = sorted(matrix)
    matrix.pop(0)

    # 같은 줄에 중복된 헥사코드 여부를 확인하여 거르기 위해
    visited = []

    # 찐 최종 진짜진짜 마지막 합계
    real_sum = 0

    # 각 번호 규칙 저장 (인덱스 번호 기준)
    rule = [[2, 1, 1], [2, 2, 1], [1, 2, 2], [4, 1, 1], [1, 3, 2], [2, 3, 1], [1, 1, 4], [3, 1, 2], [2, 1, 3],
            [1, 1, 2]]

    # 8자리 번호 입력받을 리스트
    password = []

    # 추출한 헥사코드들을 순회하며 암호코드 여부 확인
    for line in matrix:
        # 자꾸 앞에 0들이 사라져서 '0x1'을 추가함으로 0들을 살림
        h_code = '0x1' + line
        # 바이너리코드(이진수)로 변환
        bin_ = ''.join(format(int(h_code, 16), '04b')).rstrip('0')
        # 위에서 추가한 '0x1'에서의 1에 대해 생성된 4자리 바이너리코드(이진수)를 삭제
        bin_ = bin_[4:]

        # 룰에 해댕하는지 찾을 리스트
        num_check = []

        # 8자리의 암호들의 합계
        sum_password = 0

        # 특정 규칙 < (홀수위치들 * 3 + 짝수위치들) % 10 == 0 > 이 성립하는지 여부를 확인하기 위한 합계
        sum_ = 0

        # 0, 1 비율을 계산할 rate123 = r1, r2, r3
        r1, r2, r3 = 0, 0, 0

        # 위에서 변환한 바이너리코드(이진수)를 뒤에서부터 순회하며 비율체크
        for i in range(len(bin_) - 1, -1, -1):
            # 뒤에서부터 순회하므로 시작은 무조건 1, 또한 뒤에서부터 확인하므로 마지막 비율부터 카운팅
            if bin_[i] == '1' and r2 == 0:
                r3 += 1
            # 연속된 1이 끝나고 0이 나온다면 두번째 비율 카운팅
            elif bin_[i] == '0' and r1 == 0:
                r2 += 1
            # 연속된 0이 끝나고 1이 나온다면 그 다음 비율 카운팅
            elif bin_[i] == '1':
                r1 += 1
            # 연속된 1이 끝나고 나오는 0에 대해서는 큰 의미가 없으므로 흘려보냄
            elif bin_[i] == '0':
                # 의미없는 0의 순회가 끝났다면
                if bin_[i - 1] == '1':

                    # print(r1, r2, r3)

                    # 각 비율중 최저값을 찾고
                    rate = min(r1, r2, r3)

                    # 최저값으로 해당 비율들을 나누면 가장 간단한 식이 생성됨
                    num_check.append(r1 // rate)
                    num_check.append(r2 // rate)
                    num_check.append(r3 // rate)
                    # print(num_check)

                    '''
                    ex) rate = min(6,2,2)
                    rate = 2
                    6 // 2 = 3
                    2 // 2 = 1
                    2 // 2 = 1
                    즉, num_check = [3,1,1]이 생성됨
                    '''

                    # num_check의 비율이 규칙에 적용되는지 여부 확인
                    # 10가지 큐칙에 대해 순회
                    for r in range(10):
                        # 규칙과 일치한다면
                        if rule[r] == num_check:
                            # print(num_check, end=' ')
                            # print(r)

                            # 해당 번호를 합계에 추가
                            sum_password += r
                            # 해당 인덱스를 추후 특정규칙을 적용할 8자리 패스워드에 추가
                            password.append(r)
                            break

                    # 제 역할이 끝났으니 다음을 위해 초기화
                    num_check = []
                    r1, r2, r3 = 0, 0, 0

                    # 8자리가 완성되었다면
                    if len(password) == 8:
                        # 특정 규칙을 적용해보고
                        for pw in range(8):
                            if pw % 2 == 1:
                                sum_ += password[pw] * 3
                            else:
                                sum_ += password[pw]

                        # 그 규칙에 부합한다면
                        if sum_ % 10 == 0:
                            # 혹시 똑같은 패스워드가 이전에 있었는지 확인하고
                            if password not in visited:
                                # 처음 등장한 암호코드라면 합계에 추가하고
                                real_sum += sum_password
                                # 방문처리
                                visited.append(password)

                        sum_password = 0
                        sum_ = 0
                        password = []

    # 찐_최종_진짜진짜_마지막_합계
    print(f'#{tc} {real_sum}')