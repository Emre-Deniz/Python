#Red Green Blue Alpha RGBA abbrevation
from PIL import Image #library
red = Image.open("red_color.jpg") #open image
blue =Image.open("blue_color.png").convert("RGBA") #beware of image properties conversion maybe required
#alpha is opacity values between 0-255 255 is full opaque and 0 means fully transparent (image needs to opened with mode:RGBA )
red.putalpha(128) # %50 opacity
blue.putalpha(128) #%50 opacity
blue.paste(im=red,box=(0,0),mask=red) #if we paste %50 opacity images on each other we get mixture of colors
blue.save("mixed.png") #save image