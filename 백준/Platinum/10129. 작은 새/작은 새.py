import sys
def print(*args, sep=" ", end="\n"): sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

from collections import deque

def main():
    n = int(input())
    h = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        dp = deque()
        k = int(input())
        dp.append((0, 0, h[0]))
        for i in range(1, n):
            while dp and dp[0][0] + k < i: dp.popleft() 
            now = dp[0][1] + (1 if dp[0][2] <= h[i] else 0)
            while dp and (dp[-1][1] > now or dp[-1][1] == now and dp[-1][2] <= h[i]): dp.pop()
            dp.append((i, now, h[i]))
        print(dp[-1][1])
if __name__ == '__main__':
    main()