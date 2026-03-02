#include<bits/stdc++.h>
using namespace std;
using ll = long long;
vector<int> par;

int find(int x){
    if(par[x] < 0) return x;
    par[x] = find(par[x]);
    return par[x];
}

void unite(int x, int y){
    x = find(x), y = find(y);
    if(x == y) return;
    if(par[x] > par[y]) swap(x, y);
    par[x] += par[y];
    par[y] = x;
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, c, d; ll a, b; cin >> n >> a >> b >> c >> d;
    par.assign(n+1, -1);
    for(int i = 1; i <= n; i++){int x; cin >> x; unite(i, x);}
    ll m = 1; unordered_set<int> s;
    for(int i = c+1; i <= n-d; i++){
        int r = find(i);
        if(!s.insert(r).second) continue;
        m = lcm(m, -par[r]);
        if(m > b){m = b+1; break;}
    } 
    cout << (b+m-1)/m - (a+m-2)/m;
    return 0;
}