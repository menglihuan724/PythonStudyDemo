class Screen():
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,val):
        self._width=val

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,val):
        self._height=val

    @property
    def revol(self):
        return self._height*self._width

#test
dell=Screen()
dell.width=23
dell.height=33
print(dell.height)
print(dell.revol)
dell.revol=333