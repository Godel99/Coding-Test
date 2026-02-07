#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<pii> A(n);
    for(int i = 0; i < n; i++) cin >> A[i].first >> A[i].second;
    sort(A.begin(), A.end(), [](const pii& a, const pii& b){
        if(a.second != b.second) return a.second < b.second;
        return a.first < b.first;
    });
    for(int i = 0; i < n; i++) cout << A[i].first << ' ' << A[i].second << '\n';
    return 0;
}