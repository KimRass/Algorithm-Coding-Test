# include <iostream>
# include <string>

int main() {
    int n;
    std::cin >> n;

    bool exists = false;
    for (int k = 1; k < n; k++) {
        std::string str_k = std::to_string(k);
        int sum = k;
        for (int idx = 0; idx < str_k.length(); idx++) {
            int num = str_k[idx] - '0';
            sum += num;
        }
        if (sum == n) {
            exists = true;
            std::cout << k << std::endl;
            break;
        }
    }
    if (!exists) {
        std::cout << 0 << std::endl;
    }
    return 0;
}
