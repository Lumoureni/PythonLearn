# def outer(fn):
#     def inner():
#         print("Logging")
#         fn()
#     return inner
# @outer
# def send():
#     print("Over....")
# @outer
# def send2():
#     print("Over2")
#
# send()
# send2()

#-----------------------------#
# def outer(fn):
#     def inner(name):
#         print(f"{name}是inner函数中的参数")
#         print("哈哈")
#         fn(name)
#     return inner
#
# @outer
# def func(name):
#     print("这是装饰器")
#
# # 调用被装饰后的 func
# func('s')
#-----------------------------#

#-----------------------------#
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper


@my_decorator
def example():
    """This is an example function."""
    print("Hello from a function.")


print(example.__doc__)  # 输出: This is an example function.
#-----------------------------#



# def a_new_decorator(a_func):
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#
#         a_func()
#
#         print("I am doing some boring work after executing a_func()")
#
#     return wrapTheFunction
# #
# #
# # def a_function_requiring_decoration():
# #     print("I am the function which needs some decoration to remove my foul smell")
# #
# #
# # a_function_requiring_decoration()
# # # outputs: "I am the function which needs some decoration to remove my foul smell"
# #
# # a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# # # now a_function_requiring_decoration is wrapped by wrapTheFunction()
# #
# # a_function_requiring_decoration()
# # # outputs:I am doing some boring work before executing a_func()
# # #        I am the function which needs some decoration to remove my foul smell
# # #        I am doing some boring work after executing a_func()
#
#
# @a_new_decorator
# def a_function_requiring_decoration():
#     """Hey you! Decorate me!"""
#     print("I am the function which needs some decoration to "
#           "remove my foul smell")
#
#
# a_function_requiring_decoration()
# # outputs: I am doing some boring work before executing a_func()
# #         I am the function which needs some decoration to remove my foul smell
# #         I am doing some boring work after executing a_func()
#
# # the @a_new_decorator is just a short way of saying:
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
