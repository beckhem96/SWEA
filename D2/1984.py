def No_min_max_avg(N, arr):

    maxV = arr[0]
    minV = arr[0]
    maxidx, minidx = 0, 0
    for i in range(len(arr)):
        if maxV < arr[i]:
            maxV = arr[i]
            maxidx = i
    arr.pop(maxidx)
    for i in range(len(arr)):
        if minV > arr[i]:
            minV = arr[i]
            minidx = i
    arr.pop(minidx)

    sumarr = 0
    for sumV in arr:
        sumarr += sumV
    avgV = str(sumarr/len(arr))

    for i in range(len(avgV)):
        if avgV[i] == '.':
            if int(avgV[i+1]) < 5:
                avgV = int(avgV[:i])
            elif int(avgV[i+1]) >= 5:
                avgV = int(avgV[:i]) + 1
            break
    return avgV

N = int(input())
for tc in range(N):
    arr = list(map(int, input().split()))

    print(f'#{tc+1} {No_min_max_avg(N, arr)}')