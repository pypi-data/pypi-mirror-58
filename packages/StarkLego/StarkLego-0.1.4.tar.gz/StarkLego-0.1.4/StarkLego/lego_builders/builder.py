from ldraw.library.parts.others import Brick2X2
from ldraw.pieces import Group, Piece
from ldraw.figure import *
from ldraw.geometry import Identity
from ldraw.library.colours import *
import numpy as np

class Dimensions():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class LegoDimensions():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def convertToLdrDimensions(self):
        return self.x * 20, self.y * -8, self.z * 20

class BaseBlock():
    def __init__(self, x=5, y=5, z=10):
        self.group = Group()
        self.ldrContent = ""
        self.maxLdrDimensions = Dimensions(200, 120, 280)
        self.maxLegoDimensions = Dimensions(200, 120, 280)

    def append(self, newLine):
        self.ldrContent += newLine + "\n"

class LegoWorld():
    def __init__(self, x=4, y=3, z=4):
        self.group = Group()
        self.ldrContent = ""
        self.maxLegoDimensions= LegoDimensions(x, y, z)
        self.content = np.zeros([x,y,z])
        self.noOfPieces = 0
        self.yMap = np.zeros([x,z])
        self.yGlobalMax = 0
    
    def reset(self):
        self.content = np.zeros([self.maxLegoDimensions.x,self.maxLegoDimensions.y,self.maxLegoDimensions.z])
        self.ldrContent = ""
        self.noOfPieces = 0
        self.yMap = np.zeros([self.maxLegoDimensions.x, self.maxLegoDimensions.z])
        self.yGlobalMax = 0
        
    def findMaximumYValue(self, part, x, y, z):
        yGlobalMax = 0
        yOffset = 0
        for i in range(part.sizeDimensions.x):
            for j in range(part.sizeDimensions.z):
                restart = True
                while restart == True:
                    yOffset = int(self.yMap[x + i,z + j])
                    yLocalMax = int(self.yMap[x + i,z + j])
                    restart = False
                    for k in range(part.sizeDimensions.y+1):
                        if self.content[ x + i, yOffset + k, z + j] == 1:
                            if yLocalMax <= yOffset+k:    
                                yLocalMax += 1
                                self.yMap[x + i, z + j] = yLocalMax
                                restart = True  
                    if yLocalMax > yGlobalMax:
                        yGlobalMax = yLocalMax
                    if yGlobalMax > self.yGlobalMax:
                        self.yGlobalMax = yGlobalMax
        return yGlobalMax         

    def addPartToWorld(self, part, x, z):
        x = int(x)
        z = int(z)
        y = 0
        y = self.findMaximumYValue(part, x, y, z)
        for i in range(part.sizeDimensions.x):
            for j in range(part.sizeDimensions.y):
                for k in range(part.sizeDimensions.z):
                    self.content[x+i,y+j,z+k] = 1           
        self.noOfPieces += 1
        partToAdd = part.create(x, y, z, self.group)
        self.appendToLdrFile(partToAdd)

    def appendToLdrFile(self, newLine):
        self.ldrContent += newLine + "\n"

class TwoXTwoBlock():
    def __init__(self):
        self.sizeDimensions = LegoDimensions(x=2, y=3, z=2)

    def create(self, x, y, z, group):
        
        positionDimensions = LegoDimensions(x=x, y=y, z=z)
        convertedX, convertedY, convertedZ = positionDimensions.convertToLdrDimensions()
        print("adding part: ", convertedX, convertedY, convertedZ)
        return Piece(Dark_Blue, Vector(x=convertedX, y=convertedY, z=convertedZ), Identity(), Brick2X2, group).__repr__()

