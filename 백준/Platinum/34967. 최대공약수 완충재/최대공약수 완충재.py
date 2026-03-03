import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    i, j = 3, 14001
    res = []
    while i < j:
        res.append(i*j)
        res.append(i*j)
        if i+j == 14004: j -= 2
        else: i += 2
    res.pop()
    n = int(input())
    m = len(res)
    ans = []
    for k in range(n):
        if k < m: ans.append(res[k]*2)
        else: ans.append(res[m*2-1-k])
    print(' '.join(map(str, ans)))
if __name__ == '__main__':
    main()