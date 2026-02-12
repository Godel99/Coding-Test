import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

from collections import Counter

def main():
    n = int(input())
    a = []
    for _ in range(n): a.append(int(input()))
    a.sort()
    avg = sum(a) / n
    print(int(avg+0.5) if avg >= 0 else int(avg-0.5))
    print(a[len(a)//2])
    cnts = Counter(a)
    mfreq = max(cnts.values())
    freq = [i for i, v in cnts.items() if v == mfreq]
    freq.sort()
    print(freq[1] if len(freq) > 1 else freq[0])
    print(a[-1]-a[0])
    return 0
if __name__ == '__main__':
    sys.exit(main())