#Пример

#def do_twice (f):
#    f()
#    f()


#def print_spam():
#    print('спам')

#do_twice(print_spam)

#2.2

""" def do_twice(func, arg):
    func(arg)
    func(arg)

def print_message(message):
    print(message)

do_twice(print_message, "Привет!")
 """
#2.3-2.4

""" def do_twice(func, arg):
    func(arg)
    func(arg)

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, 'спам')  """

#2.5

def do_twice(f, arg):
    f(arg)
    f(arg)

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

def print_value(a):
    print(a)

do_four(print_value, "1") 


