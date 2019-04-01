class Point(object):
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    # def plus(self, other):
    #     return Point(
    #         self.__x + other.getX(),
    #         self.__y + other.getY()
    #     )

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(
                self.__x + other.getX(),
                self.__y + other.getY()
            )
        elif isinstance(other, (int, float)):
            return Point(
                self.__x + other,
                self.__y + other
            )


point = Point()

point2 = Point()

point+point2

point+4
