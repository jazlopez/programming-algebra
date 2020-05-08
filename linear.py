from src.linear import get_varname_from, rslv_linear_equation
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

    o_variable_name = get_varname_from(equality)

    result = rslv_linear_equation(equality)

    print(colorama.Fore.GREEN + "\t%s = %.2f" % (o_variable_name, result))

