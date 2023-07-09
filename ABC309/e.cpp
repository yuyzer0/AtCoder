#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); i++)
using ll = long long;
using ull = unsigned long long;
using P = pair<int, int>;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> edge(n);
    rep(i, n - 1) {
        int par;
        cin >> par;
        par--;
        int chi = i + 1;
        edge[par].push_back(chi);
    }

    vector<int> dis(n, -1);
    rep(i, m) {
        int x, y;
        cin >> x >> y;
        x--;
        dis[x] = max(dis[x], y);
    }

    auto dfs = [&](auto dfs, int u) -> void {
        for (int v : edge[u]) {
            dis[v] = max(dis[v], dis[u] - 1);
            dfs(dfs, v);
        }
    };

    dfs(dfs, 0);

    int ans = 0;
    rep(i, n) {
        if (dis[i] != -1) {
            ans++;
        }
    }

    cout << ans << endl;
    return 0;
}