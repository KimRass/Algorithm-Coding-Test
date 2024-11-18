def validate_parenthesis_string(string):
    stack = []
    for char in string:
        if char == "(":
            stack.append(1)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                return False
    else:
        return False if stack else True


if __name__ == "__main__":
    string = "s(f)g(dhh)sr)e(gdf)"
    # string = "(a(f(dcc((a))d)q)sfs)"
    print(validate_parenthesis_string(string))
