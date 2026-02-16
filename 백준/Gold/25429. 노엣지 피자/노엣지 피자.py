import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

from collections import defaultdict
        
def main():
    n, l, q = map(int, input().split())
    bucket = defaultdict(lambda: defaultdict(int))
    bucket_cnt = defaultdict(int)
    mp = defaultdict(int)
    bad = sum = 0 
    def reset_tp(x):
        nonlocal sum, bad
        if x not in mp: return
        r = x%l
        bucket[r][mp[x]] -= 1
        if bucket[r][mp[x]] == 0:
            bucket_cnt[r] -= 1
            if bucket_cnt[r] == 1: bad -= 1
            sum -= mp[x]
        del mp[x]
    for _ in range(q):
        x = tuple(map(int, input().split()))
        if x[0] == 1:
            r = x[1]%l; t = x[2]
            reset_tp(x[1])
            mp[x[1]] = t
            if bucket[r][t] == 0:
                bucket_cnt[r] += 1
                if bucket_cnt[r] == 2: bad += 1
                sum += t
            bucket[r][t] += 1
        else: reset_tp(x[1])
        if bad: print('NO')
        else: print('YES', sum)
    return 0
if __name__ == '__main__':
    sys.exit(main())