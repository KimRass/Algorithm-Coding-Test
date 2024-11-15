#include <iostream>

int main() {
    int n, m;
    std::cin >> n >> m;
    int baskets[n];
    for (int idx = 0; idx < n; idx++) {
        baskets[idx] = 0;
    }  // 배열 초기화.
    for (int _ = 0; _ < m; _++) {
        int i, j, k;
        std::cin >> i >> j >> k;
        for (int idx = i; idx <= j; idx++) {
            baskets[idx - 1] = k;
        }  // 바구니에 공을 넣음.
    }  // `m`번 사용자 입력을 받음.
    for (int idx = 0; idx < n; idx++) {
        std::cout << baskets[idx];
        if (idx != n - 1) {
            std::cout << " ";
        }
    }  // 바구니에 담긴 공을 순서대로 출력.
    return 0;
}
