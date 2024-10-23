#include <iostream>

int main() {
    int n, m;
    std::cin >> n >> m;
    int arr[n], temp[n];
    for (int idx = 0; idx < n; idx++) {
        arr[idx] = idx + 1;
    }
    std::copy(arr, arr + n, temp);
    for (int _ = 0; _ < m; _++) {
        int i, j;
        std::cin >> i >> j;
        for (int idx = i - 1; idx < j; idx++) {
            arr[idx] = temp[i + j - idx - 2];
        }
        std::copy(arr, arr + n, temp);
    }
    for (int idx = 0; idx < n; idx++) {
        std::cout << arr[idx];
        if (idx != n - 1) {
            std::cout << " ";
        }
    }
    return 0;
}
