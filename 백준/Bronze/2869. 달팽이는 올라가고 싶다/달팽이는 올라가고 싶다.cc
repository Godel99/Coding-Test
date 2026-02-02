#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    ll a, b, v; cin >> a >> b >> v;
    cout << (v-b-1)/(a-b)+1;
    return 0;
}