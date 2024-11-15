#include <iostream>
#include <unordered_map>

int main() {
    std::unordered_map<std::string, float> grade_point = {
        {"A+", 4.5},
        {"A0", 4.0},
        {"B+", 3.5},
        {"B0", 3.0},
        {"C+", 2.5},
        {"C0", 2.0},
        {"D+", 1.5},
        {"D0", 1.0},
        {"F", 0.0},
    };

    float tot_point = 0.0f;
    float sum_point = 0.0f;
    // for (int _ = 0; _ < 20; _++) {
    for (int _ = 0; _ < 3; _++) {
        std::string subject;
        float point;
        std::string grade;
        std::cin >> subject >> point >> grade;
        if (grade == "P") {
            continue;
        }
            tot_point += point * grade_point[grade];
            sum_point += point;
        std::cout << tot_point / sum_point << std::endl;
    }
    return 0;
}
