import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def dfs(ans, idx):
    global min_
    global ans_

    print(ans)

    if idx == N:
        min_ = min(min_, len(ans))
        if len(ans_) > len(ans):
            print(len(ans))
            ans_ = ans
        return

    if min_ < len(ans):
        return

    for good in inp_list[idx:]:
        found = False
        cnt = 0
        for best in ans:
            for i in range(M):
                if best[i] == good[i] or good[i] == '.' or best[i] == '.':
                    cnt += 1
                else:
                    cnt = 0
                    break

            if cnt == M:
                ans.append(good)
                if min_ < len(ans):
                    return
                dfs(ans, idx + 1)
                ans.remove(good)

                found = True
                for m in range(M):
                    if best[m] == '.' and good[m] != '.':
                        best[m] = good[m]
                dfs(ans, idx+1)

        if not found:
            ans.append(good)
            if min_ < len(ans):
                return
            dfs(ans, idx+1)


N, M = map(int, input().split())
inp_list = [list(input()) for _ in range(N)]
ans = []
ans_ = [[] for _ in range(M+1)]
min_ = float('inf')

dfs(ans, 0)

print(ans_)


# for good in inp_list:
#     found = False
#     cnt = 0
#     for best in ans:
#         for i in range(M):
#             if best[i] == good[i] or good[i] == '.' or best[i] == '.':
#                 cnt += 1
#             else:
#                 cnt = 0
#                 break
#
#         if cnt == M:
#             found = True
#             for m in range(M):
#                 if best[m] == '.' and good[m] != '.':
#                     best[m] = good[m]
#
#     if not found:
#         ans.append(good)

print(min_)
