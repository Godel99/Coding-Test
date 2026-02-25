#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int INF = 0x3f3f3f3f;

vector<int> A, T, seg, lazy, ans;

void update(int now, int l, int r, int L, int R, int x, int t){
    if(R <l || r < L) return;
    if(L <= l && r <= R){
        if(seg[now] > x){
            seg[now] = x;
            lazy[now] = max(lazy[now], t);
        }
        A[L] = seg[now];
        T[L] = lazy[now];
        return;
    }
    if(seg[now<<1] > seg[now]){
        seg[now<<1] = seg[now];
        lazy[now<<1] = max(lazy[now<<1], lazy[now]);
    }
    if(seg[now<<1|1] > seg[now]){
        seg[now<<1|1] = seg[now];
        lazy[now<<1|1] = max(lazy[now<<1|1], lazy[now]);
    }
    seg[now] = INF;
    lazy[now] = 0;
    int mid = (l+r)>>1;
    update(now<<1, l, mid, L, R, x, t);
    update(now<<1|1, mid+1, r, L, R, x, t);
}

int main(){
    cin.tie(0);cout.tie(0);ios::sync_with_stdio(0);
    int n, q; cin >> n;
    A.assign(n+1, 0);
    T.assign(n+1, 0);
    seg.assign(4*n, INF);
    lazy.assign(4*n, 0);
    for(int i = 1; i <= n; i++){
        cin >> A[i];
        update(1, 1, n, i, i, A[i], 0);        
    }
    cin >> q;
    for(int i = 1; i <= q; i++){
        int l, r, x; cin >> l >> r >> x;
        update(1, 1, n, l, r, x, i);
    }
    ans.assign(q+1, 0);
    for(int i = 1; i <= n; i++){
        update(1, 1, n, i, i, INF, 0);
        cout << A[i] << ' ';
        ans[T[i]]++;
    }
    cout << '\n';
    for(int i = 1; i <= q; i++){
        ans[i] += ans[i-1];
        cout << ans[i] << ' ';
    }
    return 0;
}