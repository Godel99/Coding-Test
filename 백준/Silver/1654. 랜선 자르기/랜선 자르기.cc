#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
    int k, n; cin >> k >> n;
    vector<ll> line(k);
    ll low = 1, high = 0;
    for(int i = 0; i < k; i++){
        cin >> line[i];
        if(high < line[i]) high = line[i];
    }
    while(low <= high){
        ll mid = (low+high)/2;
        ll total = 0;
        for(auto l : line){
            total += l/mid;
        }
        if(total >= n) low = mid+1;
        else high = mid-1;
    }
    cout << high;
    return 0;
}