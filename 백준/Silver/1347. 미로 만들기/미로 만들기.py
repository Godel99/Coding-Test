import sys

input=sys.stdin.readline

def main():
    n = int(input())
    moves = input()

    # 방향: 남(0), 동(1), 북(2), 서(3)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    x, y, d = 0, 0, 0  # 시작 위치와 방향(남쪽)
    visited = {(0, 0)}

    for move in moves:
        if move == 'F':
            x += dx[d]
            y += dy[d]
            visited.add((x, y))
        elif move == 'L':
            d = (d - 1) % 4
        else:  # 'R'
            d = (d + 1) % 4

    # 최소 직사각형 범위 계산
    min_x = min(pos[0] for pos in visited)
    max_x = max(pos[0] for pos in visited)
    min_y = min(pos[1] for pos in visited)
    max_y = max(pos[1] for pos in visited)

    # 미로 생성
    for i in range(min_x, max_x + 1):
        print(''.join('.' if (i, j) in visited else '#' 
                    for j in range(max_y, min_y - 1, -1)))

if __name__ == '__main__':
    main()