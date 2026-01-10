import sys
def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)
def input():
    return sys.stdin.readline().rstrip()

def main():
    MOD = 1000000007
    T = int(input())
    for _ in range(T):
        n = int(input())
        A = list(map(int, input().split()))
        mx = -3; mxcnt = -1; cnt = [0,0]; minus = minustwo = 0; 
        flag = 0
        for a in A:
            mx = max(mx, a)
            if a > 0: flag = 1
            if a > 1: cnt[minus] += 1
            if a < 0: minus += 1
            if a < -1: minustwo += 1
            if minus == 2:
                flag = 1
                cnt[0] += minustwo+cnt[1]
                cnt[1] = minustwo = minus = 0
            if flag: mxcnt = max(mxcnt, cnt[0], cnt[1])
            if not a: flag = cnt[0] = cnt[1] = minus = minustwo = 0
        if mxcnt < 0: print(mx); continue
        cnt[0] = cnt[1] = minus = minustwo = 0
        for a in reversed(A):
            if a > 0: flag = 1
            if a > 1: cnt[minus] += 1
            if a < 0: minus += 1
            if a < -1: minustwo += 1
            if minus == 2:
                flag = 1
                cnt[0] += minustwo+cnt[1]
                cnt[1] = minustwo = minus = 0
            if flag: mxcnt = max(mxcnt, cnt[0], cnt[1])
            if not a: flag = cnt[0] = cnt[1] = minus = minustwo = 0
        print(pow(2, mxcnt, MOD))
if __name__ == '__main__':
    main()