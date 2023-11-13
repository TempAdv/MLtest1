from PIL  import Image, ImageDraw 
import shutil
import random
import os

shutil.rmtree('TrainingExamples')
os.mkdir('TrainingExamples')
for i in range(int(input('enter number of samples'))):
    SizeX = random.randint(20,200)
    SizeY = random.randint(20,200)
    im = Image.new(mode = "RGBA",
                   size = (SizeX,SizeY),
                   color = (255, 255, 255, 255))
    
    im1 = ImageDraw.Draw(im)
    PXs = random.randint(0,SizeX-21)
    PXe = random.randint(PXs+6,SizeX)
    PYs = random.randint(0,SizeY-21)
    PYe = random.randint(PYs+6,SizeY)

    RorE = random.randint(0,1)
    if RorE == 0:
        im1.ellipse((PXs,PYs,PXe,PYe), fill ="#000000") 
        
    else:
        im1.rectangle((PXs,PYs,PXe,PYe), fill ="#000000") 

    os.mkdir(f'TrainingExamples/{i}')
    im.save(f'TrainingExamples/{i}/image.png') 
    with open(f'TrainingExamples/{i}/Data.txt', 'w') as f:
        f.write(str(RorE))
