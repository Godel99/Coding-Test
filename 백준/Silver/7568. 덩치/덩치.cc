#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<pii> p(n);
    for(int i = 0; i < n; i++) cin >> p[i].first >> p[i].second;
    for(int i = 0; i < n; i++){
        int r = 1;
        for(int j = 0; j < n; j++){
            if(p[i].first < p[j].first && p[i].second < p[j].second) r++;

        }
        cout << r << ' ';
    }
    return 0;
}