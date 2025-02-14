# ------ Package ------
# package is a collection of modules, u can install and use it
# U can install packages with Python Package Manager (PIP)
# PIP install the packeges and its related Dependencies
# Modules list websit -> https://docs.python.org/3/tutorial/modules.html
# Packages website -> https://pypi.org/
#
# in terminal: 
# 1- to check the pip version: pip --version
# 2- to list all packages: pip list
# 3- to install package or module: pip pack_name
# 4- to install package with specific version: pip pack_name = version or pip pack_name >= version
# 5- to update module: pip install --user pack_name --upgrade
# ---------------------

import termcolor, pyfiglet

# 1- some cool stufs for printing
print(pyfiglet.figlet_format("Abdullah"))

# 2- to color the output:
print(termcolor.colored("Python", color="yellow"))

# 3- compine termcolor, pyfiglet

print(termcolor.colored(pyfiglet.figlet_format("Spring"), color="green"))