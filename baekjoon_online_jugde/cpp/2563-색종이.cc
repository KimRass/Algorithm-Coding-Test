#include <iostream>

int main() {
    const int white_paper_size = 100;
    const int black_paper_size = 10;

    int paper[white_paper_size][white_paper_size];
    for (int row = 0; row < white_paper_size; row++) {
        for (int col = 0; col < white_paper_size; col++) {
            paper[row][col] = 0;
        }
    }

    int n;
    std::cin >> n;

    for (int _ = 0; _ < n; _++) {
        int x, y;
        std::cin >> x >> y;

        for (int row = y; row < y + black_paper_size; row++) {
            for (int col = x; col < x + black_paper_size; col++) {
                paper[row][col] = 1;
            }
        }
    }

    int sum = 0;
    for (int row = 0; row < white_paper_size; row++) {
        for (int col = 0; col < white_paper_size; col++) {
            sum += paper[row][col];
        }
    }
    std::cout << sum << std::endl;
    return 0;
}
