# 14502 - 연구소(G4)
import sys
from collections import deque
from copy import deepcopy


# BFS를 통해 바이러스로부터 감염될 구역 및 안전구역 count
def bfs():
    cnt = 0
    start = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                start.append((i, j))

    infected_arr = deepcopy(arr)
    queue = deque(start)
    while queue:
        n, m = queue.popleft()
        for dy, dx in dir:
            if 0 <= n + dy < N and 0 <= m + dx < M \
                    and infected_arr[n + dy][m + dx] == 0:
                infected_arr[n + dy][m + dx] = 2
                queue.append((n + dy, m + dx))
                cnt += 1

    global answer
    answer = max(answer, safe_zone - 3 - cnt)


N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

safe_zone = sum(arr, []).count(0)
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
answer = 0

# 브루트 포스 방식으로 3개의 벽을 세울 수 있는 모든 경우 확인
for i in range(N * M):
    if arr[i // M][i % M] == 0:
        arr[i // M][i % M] = 1
        for j in range(i, N * M):
            if arr[j // M][j % M] == 0:
                arr[j // M][j % M] = 1
                for k in range(j, N * M):
                    if arr[k // M][k % M] == 0:
                        arr[k // M][k % M] = 1
                        bfs()
                        arr[k // M][k % M] = 0
                arr[j // M][j % M] = 0
        arr[i // M][i % M] = 0

print(answer)
