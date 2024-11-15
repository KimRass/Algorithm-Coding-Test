#include <iostream>
#include <stack>

int main() {
    int n;
    std::cin >> n;
    std::stack<int> temp_stack;
    for (int _ = 0; _ < n; _++ ){
        int num;
        std::cin >> num;
        temp_stack.push(num);
    }

    std::stack<int> students;
    for (int _ = 0; _ < n; _++ ){
        int num = temp_stack.top();
        temp_stack.pop();
        students.push(num);
    }

    int k = 1;
    for (int _ = 0; _ < n; _++ ){
        int num = students.top();
        students.pop();
        if (num == k) {
            k += 1;
        }
        else {
            temp_stack.push(num);
        }
    }
    bool is_nice = true;
    while (!temp_stack.empty()) {
        int num = temp_stack.top();
        temp_stack.pop();
        std::cout << num << k << std::endl;
        if (num != k) {
            std::cout << "Sad" << std::endl;
            is_nice = false;
            break;
        }
        k += 1;
    }
    if (is_nice) {
        std::cout << "Nice" << std::endl;
    }
    return 0;
}
