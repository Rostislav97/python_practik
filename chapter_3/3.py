""" def setka():
    print('+', '–', '–', '–', '–','+', '–', '–', '–', '–', '+')
    print("|", ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', "|")
    print("|", ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', "|")
    print("|", ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', "|")
    print("|", ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', "|")
    print('+', '–', '–', '–', '–','+', '–', '–', '–', '–', '+')
    print("|", ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', "|")
    print("|", ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', "|")
    print("|", ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', "|")
    print("|", ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', "|")
    print('+', '–', '–', '–', '–','+', '–', '–', '–', '–', '+')

setka() """


def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def horiz_line ():
    print("+ - - - -", end=' ')

def vert_line ():
    print("|        ", end=' ')

def print_h_line ():
    do_four(horiz_line)
    print("+")

def print_v_line ():
    do_four(vert_line)
    print("|")

def half_setca():
    print_h_line()
    do_four(print_v_line)

def setca():
    do_four(half_setca)
    print_h_line()

setca()

