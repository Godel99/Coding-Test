#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; i++) cin >> a[i];
    vector<int> sorted_a = a;
    sort(sorted_a.begin(), sorted_a.end());
    sorted_a.erase(unique(sorted_a.begin(), sorted_a.end()), sorted_a.end());
    for(int i = 0; i < n; i++){
        auto idx = lower_bound(sorted_a.begin(), sorted_a.end(), a[i]);
        cout << (idx-sorted_a.begin()) << ' ';
    }
    return 0;
}