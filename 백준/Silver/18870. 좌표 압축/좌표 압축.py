import sys
print = lambda *args, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, args)) + end)
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    n = int(input())
    a = tuple(map(int, input().split()))
    sorted_a = sorted(set(a))
    dic = {v: i for i, v in enumerate(sorted_a)}
    print(*(dic[x] for x in a))
    return 0
if __name__ == '__main__':
    sys.exit(main())