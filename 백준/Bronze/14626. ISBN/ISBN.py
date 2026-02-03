import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    isbn = input()
    total = 0
    for i in range(13):
        if isbn[i] == '*': target = i; continue
        total += int(isbn[i])*(3 if i % 2 else 1)
    for i in range(10):
        if (total + i*(3 if target % 2 else 1)) % 10 == 0:
            print(i); break
    return 0
if __name__ == '__main__':
    sys.exit(main())