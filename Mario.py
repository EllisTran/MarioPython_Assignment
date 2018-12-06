from abc import ABCMeta, abstractmethod
from Sprite import Sprite

class Mario(Sprite):               #class Mario(Sprite): is an example of how to use inheritance
    #Create List for Mario imaging cycling
    marioImagesRight = []
    marioImagesLeft= []
    
    #Constructor Method
    def __init__(self, x, y, w, h, model):
        Sprite.__init__(self, x, y, w, h, model)        #Calls super constructor in sprite class
        #Initializes Member Variables
        self.jumpFrame = 0         #Checks to see how many frames Mario has jumped
        self.prevX = 0
        self.prevY = 0
        self.coinPop = 0           #Makes sure only one coin pops out
        marioImages = None

    #isSprite Abstract Methods check to see what the certain sprites are
    def isMario(self):
        return True
    def isBrick(self):
        return False
    def isCoinBlock(self):
        return False
    def isCoin(self):
        return False

    #Previous Destination Method to record the previous destination. As of now used for collision checking
    def prevDestination(self):
        self.prevX = self.x
        self.prevY = self.y
    
    #Update Method
    def update(self):
        self.model.camPos = self.x - 200        #Creates the illusion of Mario moving

        #Adds Gravity
        if self.y < 300:
            self.vert_vel +=2.1
            self.y += self.vert_vel

        #When Mario hits the ground
        if self.y >= 300:
            self.jumpFrame = 0
            self.y = 300
            self.vert_vel = 0.0
            self.coinPop = 0
        self.jumpFrame += 1
    