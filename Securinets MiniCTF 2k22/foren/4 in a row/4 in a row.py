#red, green, blue, alpha = img.split()

from PIL import Image
image = Image.open("00000000.png").convert('RGBA')
pixeldata = list(image.getdata())
flag=[]


for i,pixel in enumerate(pixeldata):
    if i % 4 ==0:
        flag.append(255 - pixel[3])
res=[chr(flag[i]) for i in range(len(flag)) if flag[i]!= 0]
print(res)
joined= "".join(res)
print(joined)
image.putdata(pixeldata)
image.save("output.png")

#Securinets{PiLl0W_Pyth0N_1S_Awe5oMe}
