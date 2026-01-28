import sys
def print(*args, sep=" ", end="\n"): sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    pos = []
    neg = []
    ones = zero = 0
    for _ in range(n):
        x = int(input())
        if x > 1: pos.append(x)
        elif x == 1: ones +=1
        elif x == 0: zero = 1
        else: neg.append(x)
    pos.sort(reverse=True)
    neg.sort()
    ans = ones
    for i in range(0, len(pos), 2):
        if i + 1 < len(pos): ans += pos[i]*pos[i+1]
        else: ans += pos[i]
    for i in range(0, len(neg), 2):
        if i + 1 < len(neg): ans += neg[i]*neg[i+1]
        else:  
            if zero == 0: ans += neg[i]
    print(ans)
    return 0
if __name__ == '__main__':
    sys.exit(main())