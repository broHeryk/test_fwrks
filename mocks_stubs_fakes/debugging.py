import os


def nice_print(item, index):
    print(f'printing item #{index}'.center(50, '-'))
    print(item)


def print_environ():
    environ = os.environ
    # import pdb; pdb.set_trace()
    breakpoint()
    for idx, item in enumerate(environ.items()):
        nice_print(item, idx)
    a = 10
    b = 20
    # breakpoint()
    return a


print_environ()

# PDB DEBUGER
# h - help
# s - step into
# n - step over
# w - stack trace
# l - piece of surrounding code
# r - move execution to the end of the function()
# unt - continue until specified line
# display - allows to see changes of expression / undisplay - removes displaying
# c -  continue to the next breakpoint


# IDE DEBUGGER
# CTRL + SHIFT + F8