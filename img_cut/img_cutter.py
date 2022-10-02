import numpy as np
from PIL import Image, ImageDraw
  
class ImgCutter:
    def __init__(self):
        pass
    def cut_image(self):
        pass

img=Image.open("img.jpeg")
  
height,width = img.size
lum_img = Image.new('L', [height,width] , 0)
  
draw = ImageDraw.Draw(lum_img)
draw.pieslice([(0,0), (height,width)], 0, 360, 
              fill = 255, outline = "white")
img_arr =np.array(img)
lum_img_arr =np.array(lum_img)
final_img_arr = np.dstack((img_arr,lum_img_arr))
output = Image.fromarray(final_img_arr)
output.save("temp.png")
