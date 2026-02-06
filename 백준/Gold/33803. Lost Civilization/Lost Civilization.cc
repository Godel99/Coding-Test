#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<pii> A;
    for(int i = 1; i <= n; i++){
        int a; cin >> a; A.emplace_back(a, i);
    }
    sort(A.begin(), A.end());
    for(int i = 0; i < n; i++) if(A[i].first > i/2) return !(cout << -1);
    for(int i = 0; i < n-2; i+=2) cout << A[i].second << ' ' << A[i+2].second << '\n';
    cout << A[n-2].second << ' ' << A[n-1].second << '\n';
    for(int i = (n%2 ? n-2 : n-1); i >= 2; i-=2) cout << A[i].second << ' ' << A[i-2].second << '\n';
    return 0;
}