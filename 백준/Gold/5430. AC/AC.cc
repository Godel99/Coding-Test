#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int t; cin >> t;
    while(t--){
        string p; cin >> p;
        int n; cin >> n;
        string x; cin >> x;
        deque<int> dq;
        string s = "";
        for(auto c : x){
            if(isdigit(c)) s += c;
            else{
                if(s.size()){
                    dq.push_back(stoi(s));
                    s = "";
                }
            } 
        }
        bool flag = 1, iser = 0;
        for(auto c : p){
            if(c == 'R') flag = !flag;
            else{
                if(dq.empty()){
                    iser = 1;
                    break;
                }
                else{
                    if(flag) dq.pop_front();
                    else dq.pop_back();
                }
            }
        }
        if(iser) cout << "error\n";
        else{
            if(dq.empty()) cout << "[]\n";
            else{
                cout << '[';
                if(flag){
                        cout << dq.front(); dq.pop_front();
                        while(dq.size()) cout << ',' << dq.front(), dq.pop_front();
                }
                else{
                    cout << dq.back(); dq.pop_back();
                    while(dq.size()) cout << ',' << dq.back(), dq.pop_back();
                }
                cout << "]\n";
            }
        }
    }
    return 0;
}