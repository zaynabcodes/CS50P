#unpacking is like spliting a value into multiple variables, * is a way of the program to split all the values in a list instead of indexing, ** for dictionares
#*args and **kwargs is the idea of having placeholders to not specify how many arguments needed for a function, it should just accept the amount entered

def f(*args, **kwargs):
    print("Named:", kwargs)

f(galleons=100, sickles=50, knuts=25) #kwargs returns a dictionary. args returns a tuple