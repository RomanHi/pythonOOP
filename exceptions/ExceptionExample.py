print("start code")

d = 0

value = 10 / d

print("это никогда не напечатается")


# print("start code")
#
# d = 0
#
# try:
#     value = 10 / d
#
#     print("value = ", value)
#
# except ZeroDivisionError as e:
#
#     print("Error: ", str(e))
#     print("Ignore to continue ...")
#
# print("теперь работате")


# class AgeException(Exception):
#
#     def __init__(self, msg, age):
#         super().__init__(msg)
#         self.age = age
#
#
# class TooYoungException(AgeException):
#
#     def __init__(self, msg, age):
#         super().__init__(msg, age)
#
#
# class TooOldException(AgeException):
#
#     def __init__(self, msg, age):
#         super().__init__(msg, age)
#
#
# def checkAge(age):
#     if age < 18:
#         raise TooYoungException("Age " + str(age) + " too young", age)
#
#     elif age > 40:
#         raise TooOldException("Age " + str(age) + " too old", age)
#
#     print("Age " + str(age) + " OK!")
#
#
# age = 20
#
# try:
#
#     checkAge(age)
#
#     d = 123 / 0
#
# except TooYoungException as e:
#
#     print("You are too young, not pass!")
#     print("Cause message: ", str(e))
#     print("Invalid age: ", e.age)
#
#
# except TooOldException as e:
#
#     print("You are too old, not pass!")
#     print("Cause message: ", str(e))
#     print("Invalid age: ", e.age)
#
# else:
#     print("You pass!")
#
# finally:
#     print("finis check age")
