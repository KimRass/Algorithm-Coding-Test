#include <iostream>

int main() {
    int n, m;
    std::cin >> n >> m;

    int arr1[n][m], arr2[n][m];
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < m; col++) {
            std::cin >> arr1[row][col];
        }
    }
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < m; col++) {
            std::cin >> arr2[row][col];
        }
    }

    for (int row = 0; row < n; row++) {
        for (int col = 0; col < m; col++) {
            std::cout << arr1[row][col] + arr2[row][col] << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}
