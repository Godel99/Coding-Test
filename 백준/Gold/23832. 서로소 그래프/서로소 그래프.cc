#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<int> phi(n+1);
    for(int i = 0; i <= n; i++) phi[i] = i;
    for(int i = 2; i <= n; i++){
        if(phi[i] == i){
            for(int j = i; j <= n; j += i) phi[j] -= phi[j]/i;
        }
    }
    ll ans = 0;
    for(int i = 2; i <= n; i++) ans += phi[i];
    cout << ans;
    return 0;
}