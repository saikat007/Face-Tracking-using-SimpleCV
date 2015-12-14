print __doc__

import os
import glob
import time
import SimpleCV
from SimpleCV import *

display = SimpleCV.Display()
c = SimpleCV.Camera()
normaldisplay = True

hc = HaarCascade("face")
while display.isNotDone():
    
    img = c.getImage().flipHorizontal()
    faces=img.findHaarFeatures(hc)

    if faces:
        face=faces[-1]
        face.draw(SimpleCV.Color.BLUE,3)

    if normaldisplay:
        img.show()
