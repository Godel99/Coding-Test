#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    vector<int> a(n+1, 0); 
    for(int i = 1; i <= n; i++){
        int t; cin >> t;
        a[i] = a[i-1]+t;
    }
    while(m--){
        int x, y; cin >> x >> y;
        cout << a[y]-a[x-1] << '\n';
    }
    return 0;
}