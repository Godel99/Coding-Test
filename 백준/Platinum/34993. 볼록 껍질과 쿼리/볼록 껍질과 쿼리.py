import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    n = int(input())
    pt = [None]*(n+1)
    qry = [None]*(n+1)
    chk = lambda i, j, idx: (qry[i][j], qry[i][j+1]) == pt[idx]
    for i in range(3, n+1, 2):
        print(f'? 3 {i-2} {i-1} {i}')
        sys.stdout.flush()
        _, *crd = map(int, input().split())
        qry[i] = crd
    for i in range(5, n+1, 2):
        for j in range(0, 6, 2):
            for k in range(0, 6, 2):
                if qry[i-2][j] == qry[i][k] and qry[i-2][j+1] == qry[i][k+1]:
                    pt[i-2] = (qry[i][k], qry[i][k+1])
            if i != 5:
                for j in range(0, 6, 2):
                    for k in range(0, 6, 2):
                        if not chk(i-2, j, i-4) and not chk(i-2, j, i-2):
                            pt[i-3] = (qry[i-2][j], qry[i-2][j+1])
    if n&1:
        print(f'? 3 1 5 {n}')
        sys.stdout.flush()
        _, *crd = map(int, input().split())
        qry[1] = crd
        for j in range(0, 6, 2):
            for k in range(0, 6, 2):
                if qry[1][j] == qry[3][k] and qry[1][j+1] == qry[3][k+1]:
                    pt[1] = (qry[1][j], qry[1][j+1])
        for j in range(0, 6, 2):
            if not chk(3, j, 1) and not chk(3, j, 3):
                pt[2] = (qry[3][j], qry[3][j+1])
        for j in range(0, 6, 2):
            for k in range(0, 6, 2):
                if qry[1][j] == qry[n][k] and qry[1][j+1] == qry[n][k+1]:
                    pt[n] = (qry[1][j], qry[1][j+1])
        for j in range(0, 6, 2):
            if not chk(n, j, n) and not chk(n, j, n-2):
                pt[n-1] = (qry[n][j], qry[n][j+1])
    else:
        print(f'? 3 1 {n-1} {n}')
        sys.stdout.flush()
        _, *crd = map(int, input().split())
        qry[1] = crd
        for j in range(0, 6, 2):
            for k in range(0, 6, 2):
                if qry[1][j] == qry[3][k] and qry[1][j+1] == qry[3][k+1]:
                    pt[1] = (qry[1][j], qry[1][j+1])
        for j in range(0, 6, 2):
            if not chk(3, j, 1) and not chk(3, j, 3):
                pt[2] = (qry[3][j], qry[3][j+1])
        for j in range(0, 6, 2):
            for k in range(0, 6, 2):
                if qry[1][j] == qry[n-1][k] and qry[1][j+1] == qry[n-1][k+1]:
                    pt[n-1] = (qry[1][j], qry[1][j+1])
        for j in range(0, 6, 2):
            if not chk(n-1, j, n-1) and not chk(n-1, j, n-3):
                pt[n-2] = (qry[n-1][j], qry[n-1][j+1])
        for j in range(0, 6, 2):
            if not chk(1, j, 1) and not chk(1, j, n-1):
                pt[n] = (qry[1][j], qry[1][j+1])
    print('!', *[v for i in range(1, n+1) for v in pt[i]])
    sys.stdout.flush()
    return 0
if __name__ == '__main__':
    sys.exit(main())