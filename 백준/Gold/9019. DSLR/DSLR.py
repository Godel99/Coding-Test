import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

from collections import deque

def main():
    t = int(input())
    mod = 10000
    for _ in range(t):
        a, b = map(int, input().split())
        dq = deque([a])
        par = [None]*mod
        par[a] = (a, "")
        while dq:
            cur = dq.popleft()
            if cur == b: break
            nxt = (cur*2)%mod
            if par[nxt] is None:
                par[nxt] = (cur, 'D')
                dq.append(nxt)
            nxt = cur-1 if cur else 9999
            if par[nxt] is None:
                par[nxt] = (cur, 'S')
                dq.append(nxt)
            nxt = (cur%1000)*10+(cur//1000)
            if par[nxt] is None:
                par[nxt] = (cur, 'L')
                dq.append(nxt)
            nxt = (cur%10)*1000+(cur//10)
            if par[nxt] is None:
                par[nxt] = (cur, 'R')
                dq.append(nxt)
        ans = []
        while b != a:
            b, cmd = par[b]
            ans.append(cmd)
        print(''.join(reversed(ans)))
if __name__ == '__main__':
    main()