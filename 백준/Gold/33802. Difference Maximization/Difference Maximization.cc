#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n , m; cin >> n >> m;
    vector<ll> A(m+1, 0); ll dmin = 0, dmax = 0;
    for(int i = 1; i <= n; i++){
        int a; cin >> a;
        if(a){
            dmin += a-1;
            dmax += m-a;
        }
        A[a]++;
    }
    ll s = 0, ans = 0;
    for(int i = 1; i < m; i++){
        s += A[i];
        ans += s*(n-A[0]-s);
    }
    while(A[0]--){
        if(dmin < dmax){
            dmin += m-1;
            ans += dmax;
        }
        else{
            dmax += m-1;
            ans += dmin;
        }
    }
    cout << ans;
    return 0;
}