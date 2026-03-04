#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int solved(int n, int r, int c){
    if(n == 0) return 0;
    int h = 1<<(n-1);
    int size = h*h;
    if(r < h && c < h) return solved(n-1, r, c);
    else if(r < h && c >= h) return size+solved(n-1, r, c-h);
    else if(r >= h && c < h) return 2*size+solved(n-1, r-h, c);
    else return 3*size+solved(n-1, r-h, c-h);
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, r, c; cin >> n >> r >> c;
    cout << solved(n, r, c);
    return 0;
}