def generate_bin_strings(n: int) -> list[str]:
    """
    """
    if n == 1:
        return ["0", "1"]

    prev = generate_bin_strings(n=n - 1)
    cur = []
    for string in prev:
        if string[-1] == "0":
            cur.append(f"{string}1")
        cur.append(f"{string}0")
    return cur


if __name__ == "__main__":
    n = 3
    bin_strings = generate_bin_strings(n)
    print(bin_strings)
