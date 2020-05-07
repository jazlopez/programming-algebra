import string
import os
import colorama

colorama.init()

os.system('clear')
print("---")
print("Programming algebra: resolve linear equations")
print("Author             : jaziel lopez github.com/jazlopez")
print("                     Tijuana Area, BC, MEXICO")
print("Instructions       : write a lineal equation and press enter")
print("                        example:")
print("                       >  2x + 1 = 11")
print("                     CTRL^C or CTRL^D to terminate program")
print("---")

while True:
    equality = input(colorama.Fore.YELLOW + " > ").replace(" ", "")
    UNK = list(filter(lambda x: x in equality, string.ascii_letters))[0]

    # tokenize
    eq_chunks = equality.split("=")
    rgt_sd_equal = eq_chunks[0]
    lft_sd_equal = int(eq_chunks[1])
    mst_lft_side = 1

    # tokenize operators
    if "+" in rgt_sd_equal:
        chunks = rgt_sd_equal.split("+")
        for chunk in chunks:
            if chunk.isdigit():
                lft_sd_equal = lft_sd_equal - float(chunk)
            else:
                try:
                    mst_lft_side = float(chunk.rstrip(UNK))
                except:
                    pass
    else:
        chunks = rgt_sd_equal.split("-")
        for chunk in chunks:
            if chunk.isdigit():
                lft_sd_equal = lft_sd_equal + float(chunk)
            else:
                try:
                    mst_lft_side = float(chunk.rstrip(UNK))
                except:
                    pass

    print(colorama.Fore.GREEN + "\t%s = %1.f" % (UNK, lft_sd_equal / mst_lft_side))
