#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    unordered_set<int> A;
    for(int i = 0; i < n; i++){
        int a; cin >> a;
        A.insert(a);
    }
    int m; cin >> m;
    vector<int> B(m);
    for(int i = 0; i < m; i++) cin >> B[i];
    for(int i = 0; i < m; i++){
        if(A.count(B[i])) cout << 1 << '\n';
        else cout << 0 << '\n';
    }
    return 0;
}