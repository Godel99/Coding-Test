#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n; cin >> n;
    if(!n) return !(cout << 0);
    vector<int> sc(n);
    for(int i = 0; i < n; i++) cin >> sc[i];
    sort(sc.begin(), sc.end());
    int exc = round(n*0.15);
    double sum = 0;
    for(int i = exc; i < n-exc; i++) sum += sc[i];
    int vsc = n-exc*2;
    if(vsc) cout << (int)round(sum/vsc);
    else cout << 0;
    return 0;
}