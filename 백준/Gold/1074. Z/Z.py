import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    n, r, c = map(int, input().split())
    ans = 0
    for i in range(n):
        ans |= (c&(1<<i))<<i
        ans |= (r&(1<<i))<<(i+1)
    print(ans)
if __name__ == '__main__':
    main()