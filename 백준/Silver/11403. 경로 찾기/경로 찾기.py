import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    for k in range(n):
        for i in range(n):
            if g[i][k]:
                for j in range(n):
                    if g[k][j]: g[i][j] = 1
    for i in range(n): print(*g[i])
if __name__ == '__main__':
    main()