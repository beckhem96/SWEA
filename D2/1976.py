# N = int(input())
# for tc in range(1, N+1):
s1 = int(input())
b1 = int(input())
s2 = int(input())
b2 = int(input())

if b1+b2 >= 60:
    if s1+s2 > 12:
        result_s = s1 + s2 - 12 + 1
    if s1+s2 <= 12:
