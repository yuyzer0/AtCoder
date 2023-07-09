#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); i++)
using ll = long long;
using ull = unsigned long long;
using P = pair<int, int>;

int main() {
    int n, k;
    cin >> n >> k;
    vector<P> ps;
    ll tot = 0;
    rep(i, n) {
        int a, b;
        cin >> a >> b;
        tot += b;
        ps.emplace_back(a, b);
    }

    if (tot <= k) {
        cout << 1 << endl;
        return 0;
    }

    sort(ps.begin(), ps.end());

    for (auto [a, b] : ps) {
        tot -= b;
        if (tot <= k) {
            cout << a + 1 << endl;
            return 0;
        }
    }

    return 0;
}