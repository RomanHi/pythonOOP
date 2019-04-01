# делит переданное число на делить
# class WrongDivider(object):
#
#     def __init__(self):
#         self.divider = 3
#
#     def divide(self, number):
#         return number / self.divider
#
#
# d = WrongDivider()
# print(d.divide(15))
# d.divider = 0
# print(d.divide(15))


class CorrectDivider(object):
    def __init__(self):
        self.__divider = 3

    def divide(self, number):
        return number / self.__divider

    def setDivider(self, val):
        if val == 0:
            print("Wrong param")
        else:
            self.__divider = val


d = CorrectDivider()
print(d.divide(15))
