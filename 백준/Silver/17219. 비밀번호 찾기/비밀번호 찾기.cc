#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m; cin >> n >> m;
    unordered_map<string, string> dic;
    for(int i = 0; i < n; i++){
        string site, pw; cin >> site >> pw;
        dic[site] = pw;
    }
    for(int i = 0; i < m; i++){
        string site; cin >> site;
        cout << dic[site]<< '\n';
    }
    return 0;
}