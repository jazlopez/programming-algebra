from src.resolve_linear_equation import find_equation_variable_name, resolve_linear_equation
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

    o_variable_name = find_equation_variable_name(equality)

    result = resolve_linear_equation(equality)

    print(colorama.Fore.GREEN + "\t%s = %.2f" % (o_variable_name, result))

