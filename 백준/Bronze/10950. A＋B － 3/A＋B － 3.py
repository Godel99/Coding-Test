import sys

input=sys.stdin.readline

def main():
    T = int(input())
    result = []
    for _ in range(T):
        a, b = map(int, input().split())
        result.append(a+b)

    for r in result:
      sys.stdout.write(f'{r}\n') 
       
if __name__ == '__main__':
    main()