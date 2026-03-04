import sys 
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    n, r, c = map(int, input().split())
    def solved(n, r, c):
        if n == 0: return 0
        h = 1<<(n-1)
        size = h*h
        if r < h and c < h: return solved(n-1, r, c)
        elif r < h and c >= h: return size+solved(n-1, r, c-h)
        elif r >= h and c < h: return 2*size+solved(n-1, r-h, c)
        else: return 3*size+solved(n-1, r-h, c-h)
    print(solved(n, r, c))
    return 0
if __name__ == '__main__':
    main()