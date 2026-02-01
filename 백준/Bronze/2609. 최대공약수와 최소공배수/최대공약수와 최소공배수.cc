#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int gcd(int a, int b){
    while(b){
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}
int lcm(int a, int b){
    return a * b / gcd(a, b);
}

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int a, b; cin >> a >> b;
    cout << gcd(a, b) << '\n' << lcm(a, b);
    return 0;
}