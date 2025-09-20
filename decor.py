# def hello():
#         print('hellloooo')
# greet = hello
# print(greet()) 
# output:hellloooo
#        None
#-------------------------------------------
# def hello(func):
#         func()
# def greet():
#         print('still here')
# a = hello(greet)
# print(a)
#output:still here
# None
#---------- high order function or HOC------------
# map()-filter()-reduce()
#------------- Decorator ----------

# def my_decorator(func):
#         def wrap_func():
#                 print('************')
#                 func()
#                 print('************')
#         return wrap_func
# @my_decorator
# def hello():
#         print('helllooooo')
# hello()
#output:
# ************
# helllooooo
# ************
#https://youtu.be/8U5zzQ8o-ko?t=1247
# @my_decorator
# def bye():
#         print("see ya later")
# bye()
# hello2 = my_decorator(hello)
# my_decorator(hello)()
#----------------------------
def my_decorator(func):
        def wrap_func(x, y):
                print('************')
                func(x, y)
                print('************')
        return wrap_func
@my_decorator

def hello(greeting, emoji):
        print(greeting,emoji )
       
        # On macOS, press Control + Command + Spacebar.
hello('hii',':)')
