#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    double sa = 0;
    vector<int> a(n);
    for(int i = 0; i < n; i++){
        cin >> a[i];
        sa += a[i];
    }
    sort(a.begin(), a.end());
    int avg = round(sa/n);
    cout << avg << '\n';
    cout << a[n/2] << '\n';
    vector<int> freq;
    int mf, cf; mf = cf = 0;
    for(int i = 0; i < n; i++){
        if(i > 0 && a[i] == a[i-1]) cf++;
        else cf = 1;
        if(cf > mf){
            mf = cf;
            freq.clear();
            freq.push_back(a[i]);
        }
        else if(cf == mf) freq.push_back(a[i]);
    }
    if(freq.size() > 1) cout << freq[1] << '\n';
    else cout << freq[0] << '\n';
    cout << a[n-1] - a[0] << '\n';
    return 0;
}