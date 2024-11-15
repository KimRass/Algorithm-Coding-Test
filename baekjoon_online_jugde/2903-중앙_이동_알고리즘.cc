#include <iostream>
#include <cmath>

int main() {
    int n;
    std::cin >> n;

    int a = 3;
    for (int _ = 0; _ < n - 1; _++) {
        a = 2 * a - 1;
    }
    int answer = std::pow(a, 2);
    std::cout << answer << std::endl;  // `std::pow` returns a `double`.
    return 0;
}
