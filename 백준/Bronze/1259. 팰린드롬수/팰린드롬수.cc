#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    string s;
    while(true){
        cin >> s; string rs(s.rbegin(), s.rend());
        if(s == "0") break;
        if(s == rs) cout << "yes" << '\n';
        else cout << "no" << '\n';
    }
    return 0;
}