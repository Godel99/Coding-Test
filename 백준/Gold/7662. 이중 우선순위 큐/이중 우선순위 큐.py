import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

import heapq

def main():
    t = int(input())
    for _ in range(t):
        k = int(input())
        max_hq, min_hq = [], []
        visited = [0]*k
        for i in range(k):
            c, v = input().split()
            if c == 'I':
                v = int(v)
                heapq.heappush(max_hq, (-v, i))
                heapq.heappush(min_hq, (v, i))
                visited[i] = 1
            else:
                if v == '1':
                    while max_hq and not visited[max_hq[0][1]]: heapq.heappop(max_hq)
                    if max_hq: visited[max_hq[0][1]] = 0; heapq.heappop(max_hq)
                else:
                    while min_hq and not visited[min_hq[0][1]]: heapq.heappop(min_hq)
                    if min_hq: visited[min_hq[0][1]] = 0; heapq.heappop(min_hq)
        while max_hq and not visited[max_hq[0][1]]: heapq.heappop(max_hq)
        while min_hq and not visited[min_hq[0][1]]: heapq.heappop(min_hq)            
        if not max_hq or not min_hq: print('EMPTY')
        else: print(-max_hq[0][0], min_hq[0][0])
if __name__ == '__main__':
    main()