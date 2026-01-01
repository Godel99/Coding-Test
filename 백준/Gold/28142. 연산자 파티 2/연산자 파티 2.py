import sys

# 0.2초 제한이므로 빠른 입출력 사용
input = sys.stdin.readline

def solve():
    try:
        line = input().strip()
        if not line: return
        N = int(line)
    except ValueError:
        return

    P = 10**9 + 7

    # 1. N 이하의 가장 큰 255의 배수를 찾음 (이 지점에서 X가 리셋됨)
    start_node = (N // 255) * 255
    
    X = 0
    current = 1

    # 2. 리셋 지점(start_node)이 0보다 크면 거기서부터 상태 설정
    if start_node > 0:
        # 255의 배수 연산(AND -> OR)을 거치면 X는 i(start_node)가 됨
        X = start_node
        
        # 단, Shift(<<) 연산은 우선순위가 가장 낮아 OR 뒤에 실행됨
        # start_node가 1023의 배수라면 Shift 적용
        if start_node % 1023 == 0:
            # X << start_node는 매우 큰 수이므로 pow(2, start_node, P) 활용
            # 문제 조건: "연산 결과가 P보다 크거나 같으면 % P"
            # start_node >= 1023 이면 2^start_node는 무조건 P보다 큼
            if X != 0:
                multiplier = pow(2, start_node, P)
                X = (X * multiplier) % P
        
        # 리셋 다음 숫자부터 시뮬레이션 시작
        current = start_node + 1

    # 3. 남은 횟수 시뮬레이션 (최대 254회 반복 -> 시간복잡도 O(1))
    for i in range(current, N + 1):
        # [우선순위 1] 빼기 (모든 i)
        X = X - i
        if X < 0:
            X = -X  # 절댓값 처리
        
        # [우선순위 2] 곱하기 (3의 배수)
        if i % 3 == 0:
            X = X * i
            if X >= P:
                X %= P
        
        # [우선순위 3] AND (15의 배수)
        if i % 15 == 0:
            X &= i
        
        # [우선순위 4] XOR (63의 배수)
        if i % 63 == 0:
            X ^= i
            
        # [우선순위 5] OR (255의 배수) 
        # (로직상 이 루프 안에서는 i % 255 == 0인 경우가 오지 않음)
        if i % 255 == 0:
            X |= i
            
        # [우선순위 6] Shift (1023의 배수)
        if i % 1023 == 0:
            # Shift는 2의 거듭제곱을 곱하는 것과 같음
            # i가 1023 이상이면 결과가 매우 크므로 모듈러 연산 필수
            if X != 0:
                multiplier = pow(2, i, P)
                X = (X * multiplier) % P

    print(X)

if __name__ == "__main__":
    solve()