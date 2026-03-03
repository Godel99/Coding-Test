import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    n = int(input())
    m = int(input())
    s = input()
    cnt = ans = 0
    i = 1
    while i < m-1:
        if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == 'I':
            cnt += 1
            if cnt >= n: ans += 1
            i += 2
        else:
            cnt = 0
            i += 1
    print(ans)

if __name__ == '__main__':
    main()