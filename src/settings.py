import turtle
import ctypes

try :
    user32 = ctypes.windll.user32
    res = width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)-70 #récupère la largeur puis la hauteur d'un écran
except :
    res = width, height = 1280, 720


class Canva():
    '''Simple class that uses the turtle module to create a canva to draw on

    Example to open the canva and close it on click when the action is done :

    canva = Canva()
    [Actions]
    canva.close()'''

    def __init__(self):
        #screen settings
        self.screen = turtle.Screen()
        self.screen.setup(width=width, height=height, startx=0, starty=0)
        self.screen.screensize(2*width,2*height)
        self.screen.bgcolor('black')
        self.screen.delay(0)

        #basic drawing settings
        self.draw = turtle.Turtle()
        self.draw.speed(0)
        self.draw.setpos(width//6-200, - height//4-50)
        self.draw.color('green')

    #close method on click
    def close(self):
        self.screen.exitonclick()