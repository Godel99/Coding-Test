#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, k; cin >> n >> k;
    if(k > n/2) k = n-k;
    int ans = 1;
    for(int i = 1; i <= k; i++) ans = ans*(n-i+1)/i;
    cout << ans;
    return 0;
}