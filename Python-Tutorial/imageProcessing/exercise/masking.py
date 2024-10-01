from PIL import Image #import library
words = Image.open("word_matrix.png") #open images
mask = Image.open("mask.png")

w,h = words.size #take size of words
mask = mask.resize((w,h)) #resize mask to match size of words

mask.putalpha(128) #make it transparent so words below can be seen
words.paste(im=mask,box=(0,0),mask=mask) #put mask on the words
words.save("newWord_matrix.png") #save result