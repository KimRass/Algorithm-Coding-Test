#include <iostream>
#include <cstdlib>
#include <vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> balloons(n);
    std::vector<bool> is_bursted(n, false);
    for (int idx = 0; idx < n; idx++) {
        std::cin >> balloons[idx];
    }

    int idx = 0;
    for (int stage = 0; stage < n; stage++) {
        std::cout << idx + 1 << " ";

        int rem_steps = balloons[idx];
        is_bursted[idx] = true;

        int direc = (rem_steps > 0) ? 1 : -1;

        if (stage == n - 1) break;

        while (rem_steps != 0) {
            idx = ((idx + direc) % n + n) % n;  // Ensure idx is within bounds.
            if (!is_bursted[idx]) {
                rem_steps -= direc;
            }
        }
    }
    return 0;
}
// 3 2 1 -3 -1 -> 1 4 5 3 2
