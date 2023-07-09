#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); i++)
using ll = long long;
using ull = unsigned long long;
using P = pair<int, int>;

int main() {
    int n1, n2, m;
    cin >> n1 >> n2 >> m;
    int n = n1 + n2;
    vector<vector<int>> edge(n);
    rep(i, m) {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        edge[a].push_back(b);
        edge[b].push_back(a);
    }

    auto bfs = [&](int sv) {
        vector<int> dist(n, -1);
        queue<int> q;
        q.push(sv);
        dist[sv] = 0;
        int max_dis = 0;
        while (!q.empty()) {
            int u = q.front();
            max_dis = max(max_dis, dist[u]);
            q.pop();
            for (int v : edge[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
                }
            }
        }
        return max_dis;
    };

    cout << bfs(0) + bfs(n - 1) + 1 << endl;
    return 0;
}