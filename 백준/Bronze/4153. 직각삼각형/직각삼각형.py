def main():
    while True:
        tri = list(map(int, input().split()))
        if tri == [0,0,0]:
            break
        tri.sort()
        a,b,c = tri
        if pow(c, 2) == (pow(a, 2) + pow(b, 2)):
            print('right')
        else:
            print('wrong') 

    
if __name__ == '__main__':
    main()