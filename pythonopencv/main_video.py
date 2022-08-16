def get_num(seq, n):
    if seq[0] == "0":
        return get_num(seq[1:], n - 1)
    elif seq[0] == "1":
        return get_num(seq[2:], n - 2) + ans[n - 1]