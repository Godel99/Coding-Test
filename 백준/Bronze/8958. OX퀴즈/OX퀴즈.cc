#include<bits/stdc++.h>
using namespace std;

int main(){
   int T; cin >> T;

   for(int i=0; i<T; i++){
        string s; cin >> s;
        int total = 0, cnt = 0;
        for(int j=0; j<s.size(); j++){
            if(s[j]=='O'){
                cnt++;
                total += cnt;
            }
            else cnt = 0;
        }
        cout << total << endl;
   }
}