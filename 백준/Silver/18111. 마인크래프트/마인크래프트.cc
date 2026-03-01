#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int inf = 0x3f3f3f3f;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n, m, b; cin >> n >> m >> b;
    int min_h = 256, max_h = 0;
    vector<int> height(257, 0);
    for(int i = 0; i < n; i++) for(int j = 0; j < m; j++){
        int h; cin >> h;
        if(min_h > h) min_h = h;
        if(max_h < h) max_h = h;
        height[h]++;
    }
    int min_t = inf, best_h = 0; 
    for(int tar = min_h; tar <= max_h; tar++){
        int up, down; up = down = 0;
        for(int h = min_h; h <= max_h; h++){
            if(h > tar) down += (h-tar)*height[h];
            else up += (tar-h)*height[h];
        }
        if(down+b >= up){
            int cur_t = down*2+up;
            if(cur_t <= min_t){
                min_t = cur_t;
                best_h = tar;
            }
        }
    }
    cout << min_t << ' ' << best_h;
    return 0;
}