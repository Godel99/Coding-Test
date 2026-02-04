#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    for(int j = 0; j < 3; j++){
        string s; cin >> s;
        if(isdigit(s[0])){
            int i = stoi(s)+3-j;
            if(i % 3 == 0 && i % 5 == 0) cout << "FizzBuzz";
            else if(i % 3 == 0 && i % 5 != 0) cout << "Fizz";
            else if(i % 3 != 0 && i % 5 == 0) cout << "Buzz";
            else cout << i;
            break;
        }
    }
    return 0;
}