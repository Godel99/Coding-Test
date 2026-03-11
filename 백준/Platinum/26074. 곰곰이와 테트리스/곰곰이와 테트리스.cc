#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    if(n > m) swap(n, m);
    cout << (n == 1 && m == 2 ? "ChongChong" : "GomGom");
    return 0;
}