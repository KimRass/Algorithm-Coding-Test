#include <vector>
#include <iostream>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> scores(n);
    for (int idx = 0; idx < n; idx++) {
        std::cin >> scores[idx];
    }
    float max_score = *std::max_element(scores.begin(), scores.end());
    float sum = 0.0f;  // Specifying `0.0f` ensures the initial value is a `float`. Using just `0` would represent an `int`, and `0.0` represents a `double`. By using 0.0f
    for (int idx = 0; idx < n; idx++) {
        sum += scores[idx] / max_score * 100;
    }
    std::cout << sum / n << std::endl;
    return 0;
}
