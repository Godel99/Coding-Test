import sys
def print(*args, sep=" ", end="\n"): sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    words = [input().strip() for _ in range(n)]
    weight = {}
    for word in words:
        p = 1
        for c in word[::-1]:
            weight[c] = weight.get(c, 0)+p
            p *= 10
    vals = sorted(weight.values(), reverse=True)
    num = 9
    ans = 0
    for val in vals:
        ans += num*val
        num -= 1
    print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())