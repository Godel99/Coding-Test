from math import sqrt

def isprime(n): # 소수를 판별하는 함수
    if n<=1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    cnt = 0
    for x in num_list:
        if isprime(x):
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()