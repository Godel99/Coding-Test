import sys
def print(*args, sep=" ", end="\n"): return sys.stdout.write(sep.join(map(str, args)) + end)
def input(): return sys.stdin.readline().rstrip()

def main():
    for j in range(3):
        s = input()
        if s.isdigit():
            i = int(s)+3-j
            if i % 3 == 0 and i % 5 == 0: print('FizzBuzz')
            elif i % 3 == 0 and i % 5 != 0: print('Fizz')
            elif i % 3 != 0 and i % 5 == 0: print('Buzz')
            else: print(i)
            break 
    return 0
if __name__ == '__main__':
    sys.exit(main())