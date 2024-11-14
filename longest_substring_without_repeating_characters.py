def solve(s):
    left = 0
    unique_chars = set()
    max_len = 0
    for right in range(len(s)):
        while s[right] in unique_chars:
            unique_chars -= {s[left]}
            left += 1
        unique_chars.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len


if __name__ == "__main__":
    s = "kwweaesdc"
    # k, {}
    # kw, {k}
    # kww: x, {k, w}
    # w
    # we
    # wea
    # weae: x
    # ae
    # aes
    # aesd
    # aesdc
    solve(s)
