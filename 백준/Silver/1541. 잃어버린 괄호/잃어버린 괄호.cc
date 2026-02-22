#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int sum_group(string seg){
    int res = 0;
    stringstream ss(seg);
    string token;
    while(getline(ss, token, '+')){
        res += stoi(token);
    }
    return res;
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    string s, seg; cin >> s;
    stringstream ss(s);
    vector<int> sumx;
    while(getline(ss, seg, '-')){
        sumx.push_back(sum_group(seg));
    }
    int ans = sumx[0];
    for(int i = 1; i < sumx.size(); i++) ans -= sumx[i];
    cout << ans;
}