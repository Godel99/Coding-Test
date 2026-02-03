#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    string isbn; cin >> isbn;
    int target, total = 0;
    for(int i = 0; i < 13; i++){
        if(isbn[i] == '*'){ 
            target = i; continue;
        }
        total += (isbn[i]-'0')*(i % 2 ? 3 : 1);
    }
    for(int i = 0; i < 10; i++){
        if((total + i*(target % 2 ? 3 : 1)) % 10 == 0){
            cout << i; break;
        }
    }
    return 0;
}