def main():
    T = int(input())
    for _ in range(T):
        H, _, N = map(int, input().split())
        floor = N % H
        room = (N // H) + 1
        
        if floor == 0:
            floor = H
            room -= 1
        
        print(f'{floor}{room:02d}')

if __name__ == '__main__':
    main()
