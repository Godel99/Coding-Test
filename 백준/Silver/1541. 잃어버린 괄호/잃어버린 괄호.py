import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    ops = input().split('-')
    sumx = []
    for op in ops: sumx.append(sum(map(int, op.split('+'))))
    ans = sumx[0]
    for i in range(1, len(sumx)): ans -= sumx[i]
    print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())