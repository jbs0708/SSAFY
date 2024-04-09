# 크기 입력받기
N = int(input())

# 배열생성
list_ = [list(map(int, input().split())) for _ in range(N)]

# 최대최소 변수 생성(좌표의 크기가 1000이므로 각 절대값 1001을 부여)
xMax = -1001
yMax = -1001
xMin = 1001
yMin = 1001

# 최대최소 찾기
for x,y in list_:
    if x > xMax:
        xMax = x
    if x < xMin:
        xMin = x
    if y > yMax:
        yMax = y
    if y < yMin:
        yMin = y

# 각 축을 기준으로 최대 길이 찾기
xLen = xMax - xMin
yLen = yMax - yMin
maxLen = max(xLen, yLen)

# 정사각형이 가능한지 불가능한지 체크 (추후 *양사이드 체크와 *리스트합계 체크로 확인)
check = True

# *양사이트 체크를 위한 bool 변수
sideMax = False
sideMin = False

## 메인 로직 ##
# 각 축의 차이가 같다면
if xLen == yLen:
    for i in list_:
        if i[1] == yMax or i[1] == yMin:
            i[1] = 0
            i[0] = 0
        if i[0] == xMax or i[0] == xMin:
            i[0] = 0
            i[1] = 0
elif yLen > xLen:
    for i in list_:
        if i[1] == yMax or i[1] == yMin:
            i[1] = 0
            i[0] = 0
        else:
            if i[0] == xMax:
                i[0] = 0
                i[1] = 0
                sideMax = True
            elif i[0] == xMin:
                i[0] = 0
                i[1] = 0
                sideMin = True
else:
    for i in list_:
        if i[0] == xMax or i[0] == xMin:
            i[0] = 0
            i[1] = 0
        else:
            if i[1] == yMax:
                i[0] = 0
                i[1] = 0
                sideMax = True
            elif i[1] == yMin:
                i[0] = 0
                i[1] = 0
                sideMin = True

if sideMin and sideMax:
    check = False

if sum(sum(list_,[])) != 0:
    check = False

if check:
    print(maxLen)
else:
    print(-1)