class Colour:
    def __init__(self,red,blue,green):
        self.red=red
        self.green=green
        self.blue=blue
    def display(self):  #use identation to define the method if object is to be used
     print("Colour:",colour.red,colour.green,colour.blue )

colour= Colour(255,123,53)
colour.display()