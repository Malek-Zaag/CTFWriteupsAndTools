#red, green, blue, alpha = img.split()

from PIL import Image
image = Image.open("00000000.png").convert('RGBA')
pixeldata = list(image.getdata())




px = image.load()
flag=""
for i in range(150):
    for j in range(150):
        if (i==j) and (i % 5 ==0):
            flag+=chr(255 - px[i,i][-1]^(px[i,i][0]^((px[i,i][1] + px[i,i][2])%3)))

print(flag)
image.save("output.png")

#Securinets{AlpH4_1S_vEry_H4rD}
