import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n, q = map(int, input().split()); idx = n
    a = [0]*(n+q+1)
    cnt = [0]*32
    e = 0
    for i, v in enumerate(map(int, input().split())): 
        a[i+1] = v
        for bit in range(32):
            if a[i+1]&(1<<bit): cnt[bit] += 1
    for _ in range(q):
        query = tuple(map(int, input().split()))
        t = query[0]
        if t == 1:
            idx += 1
            v = query[1]^e
            a[idx] = v
            for bit in range(32):
                if a[idx]&(1<<bit): cnt[bit] += 1
            n += 1
        elif t == 2:
            p = query[1]
            for bit in range(32):
                if a[p]&(1<<bit): cnt[bit] -= 1
            n -= 1
        else:
            e ^= query[1]
        ans = 0
        for bit in range(32):
            if e&(1<<bit): ans += (n-cnt[bit])<<bit
            else: ans += cnt[bit]<<bit
        print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())