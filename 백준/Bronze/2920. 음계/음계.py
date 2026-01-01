import sys

def main():
    ascending = [i for i in range(1, 9)]
    descending = [i for i in range(8, 0, -1)]
    n = list(map(int, input().split()))

    if n == ascending:
        sys.stdout.write('ascending\n')
    elif n == descending:
        sys.stdout.write('descending\n')
    else:
        sys.stdout.write('mixed\n')

if __name__ == '__main__':
    main()