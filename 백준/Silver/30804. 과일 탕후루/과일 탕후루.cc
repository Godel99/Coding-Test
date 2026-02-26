#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; i++) cin >> a[i];
    vector<int> cnt(10, 0);
    int l, t, maxl; l = t = maxl = 0;
    for(int r = 0; r < n; r++){
        cnt[a[r]]++;
        if(cnt[a[r]] == 1) t++;
        while(t > 2){
            cnt[a[l]]--;
            if(cnt[a[l]] == 0) t--;
            l++;
        }
        maxl = max(maxl, r-l+1);
    }
    cout << maxl;
    return 0;
}