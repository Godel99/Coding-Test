import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from collections import deque

def main():
    n, k = map(int, input().split())
    if n == k: print(0); return
    maxl = (n if n > k else k)+2
    dp = [0]*maxl
    dq = deque([n])
    while dq:
        cur = dq.popleft()
        for nxt in [cur-1, cur+1, cur*2]:
            if 0 <= nxt < maxl and not dp[nxt]:
                dp[nxt] = dp[cur]+1
                dq.append(nxt)
    print(dp[k])
if __name__ == '__main__':
    main()