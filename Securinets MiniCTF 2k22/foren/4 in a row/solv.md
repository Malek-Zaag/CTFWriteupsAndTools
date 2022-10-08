# 4 in a row

<img src="https://github.com/Malek-Zaag/CTF-Writeups/blob/main/Securinets%20MiniCTF%202k22/foren/4%20in%20a%20row/1_tgsyoUuus_3tEXpag0ArJw.png">

The challenge was given as a 150x150 png file and as the description mentioned it was about png color channels and specifically the alpha value of a pixel.

<img src="https://github.com/Malek-Zaag/CTF-Writeups/blob/main/Securinets%20MiniCTF%202k22/foren/4%20in%20a%20row/1_wXgoEdJu-twI8R4gFJWrkg.png">

We can read from the description that the flag was hidden in the alpha value of every pixel that its order is divisible by 4 . But before we jump to the extracting part let’s talk about the png color channel and how the data is embeded in each pixel.Each pixel in an image is represented by the model RGBA(red,green,blue,alpha) and these pixels are presenting the image as a matrix.

So the description says that the author is hidding the flag in the diagonal pixels and he gives the formula to extract it , so i concluded with a script doing it

```python
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

```

and the flag is Securinets{PiLl0W_Pyth0N_1S_Awe5oMe}
