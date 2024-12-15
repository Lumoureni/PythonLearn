#try->except->else->finally

# def get_exception():
#      a = 1 / 0
# def get_exception2():
#     get_exception()
# def get_exception3():
#     get_exception2()
# get_exception3()
#执行逻辑由下往上

# try:
#     a = 1/0
# except ZeroDivisionError as e:
#     print("不能被0正常")
# else:
#     print("输出正常")
# finally:
#     print("已执行结束")

# import sys
#
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

# x = 10
# if x > 5:
#     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

# class Error(Exception):
#     """Base class for exceptions in this module."""
#     pass
#
# class InputError(Error):
#     """Exception raised for errors in the input.
#
#     Attributes:
#         expression -- input expression in which the error occurred
#         message -- explanation of the error
#     """
#
#     def __init__(self, expression, message):
#         self.expression = expression
#         self.message = message
#
# class TransitionError(Error):
#     """Raised when an operation attempts a state transition that's not
#     allowed.
#
#     Attributes:
#         previous -- state at beginning of transition
#         next -- attempted new state
#         message -- explanation of why the specific transition is not allowed
#     """
#
#     def __init__(self, previous, next, message):
#         self.previous = previous
#         self.next = next
#         self.message = message