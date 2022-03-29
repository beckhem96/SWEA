import sys

sys.stdin = open('1859_백만장자프로젝트.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    things = list(map(int, input().split()))
    cal = []
    result = 0
    i = 0
    while i < N:
        if i == N -1:
            break
        maxV = max(things[i:])

        i = things.index(maxV)
        for j in range(len(things[:i]), 0, -1):
            result += maxV - things[i-j]
        i += 1

    print(result)


    print(f'#{tc} {result}')