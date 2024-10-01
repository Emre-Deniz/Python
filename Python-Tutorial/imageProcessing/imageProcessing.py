from PIL import Image #PIL python image library
pencilImage= Image.open("pencils.jpg") #taking an image note needs to be in same directory or enter path

#printing various information
print(pencilImage.size)
print(pencilImage.format)
print(pencilImage.filename)
print(pencilImage.format_description)
print(pencilImage)
#cropping an image
width,height=pencilImage.size #assing image size to variables
width=width/3 # I just want to crop this images unvanted side-in this case just pencils 

croppedPencil=pencilImage.crop((0,0,width,height)) 
#pencil images pixels starts from upper left corner 0,0 means that position 
#width,height means how many pixels to shift right with width value and shift below with height value from given starting position
croppedPencil.save("croppedPencil.jpg") #to save new image as a file to current directory

rotatedCroppedPencil = croppedPencil.rotate(180) #rotate image counter clockwise
rotatedCroppedPencil.save("rotatedCroppendPencil.jpg") #save image

pencilImage.paste(im=rotatedCroppedPencil,box=(int(width),0)) #we can paste images on others beware if you are worked with values they can become float and maybe needs conversion
pencilImage.save("newPencilImage.jpg") #so long as we DONT enter same name of files they are safe from overwriting

pencilImage.resize(500,500) #images can be resized

