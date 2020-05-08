import string


def get_varname_from(equality):

    """
    :param equality:
    :return:
    """

    return list(filter(lambda x: x in equality, string.ascii_letters))[0]


def rslv_linear_equation(equality):

    """
    :param equality:
    :return:
    """

    unk = get_varname_from(equality)

    # tokenize
    eq_chunks = equality.split("=")
    rgt_sd_equal = eq_chunks[0]
    lft_sd_equal = int(eq_chunks[1])
    mst_lft_side = None

    # tokenize operators
    if "+" in rgt_sd_equal:
        chunks = rgt_sd_equal.split("+")
        for chunk in chunks:
            if chunk.isdigit():
                lft_sd_equal = lft_sd_equal - float(chunk)
            else:
                try:
                    mst_lft_side = float(chunk.rstrip(unk))
                except:
                    pass
    else:
        chunks = rgt_sd_equal.split("-")
        for chunk in chunks:
            if chunk.isdigit():
                lft_sd_equal = lft_sd_equal + float(chunk)
            else:
                try:
                    mst_lft_side = float(chunk.rstrip(unk))
                except:
                    pass

    return float("%.2f" % (lft_sd_equal / mst_lft_side))
