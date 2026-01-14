import sys
def print(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(map(str, args)) + end)
def input():
    return sys.stdin.readline().rstrip()

def josephus(n, k):
    if n == 1: return 0
    
    # i: 현재 인원 수 (1명부터 시작)
    # res: 현재 생존자의 인덱스 (0-based)
    res = 0
    i = 1
    
    while i < n:
        # 1. 한 번에 건너뛸 수 있는 최대 크기(step) 계산
        # 공식: 현재 남은 거리(i - res - 1)를 (k-1)로 나눈 몫
        # 의미: 인덱스(res)가 k만큼 증가해도 원의 크기(i)를 넘어서 '한 바퀴 돌지 않는' 안전 구간
        step = (i - res - 1) // (k - 1)
        
        # 2. 최소 1칸은 진행해야 함 (step이 0이면 1로 강제)
        if step == 0:
            step = 1
            
        # 3. 목표인 n을 넘지 않도록 조정
        if i + step > n:
            step = n - i
            
        # 4. 상태 업데이트
        # 인덱스는 k * step 만큼 증가
        res = res + (step * k)
        # 인원 수는 step 만큼 증가
        i = i + step
        # 원형 구조이므로 모듈러 연산
        res = res % i
        
    return res

def main():
    n, k = map(int, input().split())
    print(n) if k == 1 else print(josephus(n,k)+1)
if __name__ == '__main__':
    main()