import sys

def main():
    s = set()
    n = [int(input()) for _ in range(10)]
    
    for i in n:
        s.add(i%42)

    sys.stdout.write(str(len(s)))

if __name__ == '__main__':
    main()