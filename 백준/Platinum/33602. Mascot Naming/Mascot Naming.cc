#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<string> s(n);
    for(int i = 0; i < n; i++) cin >> s[i];
    string t; cin >> t;
    vector<vector<char>> ch(t.size());
    for(int i = 0; i < n; i++){
        int r = 0;
        for(char c : s[i]){
            if(c == t[r]){
                r++;
                if(r == t.size()){
                    cout << "NO";
                    return 0;
                }
            }
            else ch[r].push_back(c);
        }
    }
    cout << "YES\n";
    for(int i = 0; i < t.size(); i++){
        for(char c : ch[i]) cout << c;
        if(i < t.size()-1) cout << t[i];
    }
    return 0;
}