#include <iostream>
#include <string>

int main() {
    std::string str;
    std::cin >> str;
    int is_palindrome = 1;
    for (int idx = 0; idx < str.length() / 2; idx++) {
        if (str[idx] != str[str.length() - 1 - idx]) {
            is_palindrome = 0;
            break;
        }
    }
    std::cout << is_palindrome << std::endl;
    return 0;
}
