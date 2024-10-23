#include <iostream>
#include <algorithm>

int main() {
    int a, b, c;
    std::cin >> a >> b >> c;
    if (a == b && b == c) {
        std::cout << 10000 + a*1000 << std::endl;
    } else if (a == b || b == c) {
        std::cout << 1000 + b*100 << std::endl;
    } else if (a == c) {
        std::cout << 1000 + a*100 << std::endl;
    } else {
        std::cout << std::max(std::max(a, b), c)*100 << std::endl;
    }
    return 0;
}
