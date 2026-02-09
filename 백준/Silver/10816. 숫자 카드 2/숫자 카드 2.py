import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

from collections import Counter

def main():
    n = int(input())
    cards = Counter(input().split())
    m = int(input())
    queries = input().split()
    print(' '.join(str(cards[query]) for query in queries))
    return 0
if __name__ == '__main__':
    sys.exit(main())