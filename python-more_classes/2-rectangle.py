class Rectangle:
    def __init__(self, width=0, heigth=0):
        self.width = width
        self.heidth = heigth
    
    #Property getter for width
    @property
    def width(self):
        return self.self.__width
    
    #Property setter for width
    @width.setter
    def width