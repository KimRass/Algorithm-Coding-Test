#include <iostream>
#include <string>

int main() {
    int n;
    std::cin >> n;
    for (int _ = 0; _ < n; _++) {
        std::string str;
        std::cin >> str;
        std::cout << str.front() << str.back() << std::endl;
    }
    return 0;
}
