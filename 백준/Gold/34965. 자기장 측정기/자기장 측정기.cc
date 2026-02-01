#include<bits/stdc++.h>
using namespace std;
using ll = long long;

ll dist(ll x, ll y){
    if(x < 0) x = -x; if(y < 0) y = -y;
    return x*x + y*y;
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int dx[] = {1, 0, -1, 0}, dy[] = {0, 1, 0, -1};
    ll sx, sy; cin >> sx >> sy; if(!sx && !sy) return !(cout << -1);
    ll x = -sx, y = -sy;
    ll ax = x, ay = y;
    string s; cin >> s;
    int idx = 0, dir = 0;
    while(idx < s.length()){
        char op = s[idx++];
        int d = 0;
        while(isdigit(s[idx])) d = d*10+s[idx++]-'0';
        if(op == 'S'){
            ll nx = x+d*dx[dir], ny = y+d*dy[dir];
            if(x*nx <= 0 && y*ny <= 0) return !(cout << -1);
            if(dist(nx, ny) < dist(ax, ay)) ax = nx, ay = ny;
            if(x*nx < 0) if(dist(0, y) < dist(ax, ay)) ax = 0, ay = y;
            if(y*ny < 0) if(dist(x, 0) < dist(ax, ay)) ax = x, ay = 0;
            x = nx, y = ny;
        }
        if(op == 'T'){
            dir += d, dir %= 4;
        }
    }
    cout << ax+sx << ' ' << ay+sy;
    return 0;
}