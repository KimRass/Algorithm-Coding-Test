#include <iostream>

int main() {
    int n, m;
    std::cin >> n >> m;
    int basket[n];
    for (int idx = 0; idx < n; idx++) {
        basket[idx] = 0;
    }
    for (int _ = 0; _ < m; _++) {
        int i, j, k;
        std::cin >> i >> j >> k;
        for (int idx = i; idx <= j; idx++) {
            basket[idx - 1] = k;
        }
    }
    for (int idx = 0; idx < n; idx++) {
        std::cout << basket[idx];
        if (idx != n - 1) {
            std::cout << " ";
        }
    }
    return 0;
}
