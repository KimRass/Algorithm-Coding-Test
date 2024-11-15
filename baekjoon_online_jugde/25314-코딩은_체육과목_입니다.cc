#include <iostream>

int main() {
    int n, k;
    std::cin >> n;
    k = n / 4;
    for (int _ = 0; _ < k; _++) {
        std::cout << "long ";
    }
    std::cout << "int" << std::endl;
    return 0;
}
