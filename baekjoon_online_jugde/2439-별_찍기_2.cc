#include <iostream>

int main() {
    int n;
    std::cin >> n;
    for (int k = 1; k <= n; k++) {
        for (int _ = n - k; _ > 0; _--) {
            std::cout << " ";
        }
        for (int _ = 0; _ < k; _++) {
            std::cout << "*";
        }
        std::cout << std::endl;
    }
    return 0;
}
