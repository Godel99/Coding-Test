#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    cout << (n == 1 && m == 2 || n == 2 && m == 1 ? "ChongChong" : "GomGom");
    return 0;
}