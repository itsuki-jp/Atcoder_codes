class Shape:
    """
    面積と周りの長さを計算する
    """

    def __init__( self, width=10, height=10 ):
        self.width = width
        self.height = height

    def area( self ):
        print(f"area : {self.width * self.height}")

    def perimeter( self ):
        print(f"perimeter : {self.width * 2 + self.height}")


s = Shape(10, 20)
s.area()
s.perimeter()
