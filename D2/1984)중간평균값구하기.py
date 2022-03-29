import sys


sys.stdin = open('1984_중간평균값구하기.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    nums.sort()
    nums = nums[1:-1]
    result = round(sum(nums)/len(nums))
    print(f'#{tc} {result}')