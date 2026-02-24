#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
    int n; ll m; cin >> n >> m;
    vector<ll> tree(n);
    ll low, high; low = high = 0;
    for(int i = 0; i < n; i++){ 
        cin >> tree[i];
        if(high < tree[i]) high = tree[i];
    }
    while(low <= high){
        ll mid = (low+high)/2;
        ll total = 0;
        for(auto t : tree){
            if(t > mid) total += t-mid;
        }
        if(total >= m) low = mid+1;
        else high = mid-1;
    }
    cout << high;
    return 0;
}