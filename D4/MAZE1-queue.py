def bfs(i, j): # 미로의 도착여부 확인
    visited = [[0]*16 for _ in range(16)]# visited 생성
    q = []   # 큐 생성
    q.append((i, j)) # 시작점 인큐
    visited[i][j] = 1 # 시작점 방문 표시
    while q:  # 큐가 비어있지 않으면
        i, j = q.pop(0) # 디큐
        if arr[i][j] == 3: # 도착하면
            return 1
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            # 항상 벽으로 둘러쌓인 미로이므로 0<=ni<16 and 0<=nj<16 생략 가능
            if arr[ni][nj] != 1 and visited[ni][nj] == 0:# 벽이 아니고 방문한 적이 없으면
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1 # 거리가 필요한 경우
                # visited[ni][nj] = 1 # 거리 필요없으면 이렇게 해도됨
    return 0 # 도착 못하는 경우
for _ in range(10):
    N = 16
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    sti = -1
    stj = -1
    for i in range(16): # 출발 위치 찾기
        for j in range(16):
            if arr[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break
    print(f'#{tc} {bfs(sti, stj)}')