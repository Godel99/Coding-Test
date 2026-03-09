#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, k; cin >> n >> k;
    cout << "YES\n";
    for(int i = 1; i < k; i++) cout << i << ' ';
    for(int i = n; i >= k; i--) cout << i << ' ';
    return 0;
}