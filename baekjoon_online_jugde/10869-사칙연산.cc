#include <iostream>

int main() {
    int a, b, plus, minus, multi, quotient, remainder;
    std::cin >> a >> b;
    plus = a + b;
    minus = a - b;
    multi = a * b;
    quotient = a / b;
    remainder = a % b;
    std::cout << plus << std::endl;
    std::cout << minus << std::endl;
    std::cout << multi << std::endl;
    std::cout << quotient << std::endl;
    std::cout << remainder << std::endl;
    return 0;
}
