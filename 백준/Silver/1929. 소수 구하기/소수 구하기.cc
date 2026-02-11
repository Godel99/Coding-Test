#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int m, n; cin >> m >> n;
    vector<bool> p(n+1, true); p[0]=p[1]=false;
    for(int i = 2; i <= sqrt(n); i++){
        if(p[i]){
            for(int j = i*i; j <= n; j+=i) p[j] = false;
        }
    }
    for(int i = m; i <= n; i++) if(p[i]) cout << i << '\n';
    return 0;
}