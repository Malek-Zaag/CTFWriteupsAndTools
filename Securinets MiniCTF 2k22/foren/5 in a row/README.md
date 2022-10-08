# 5 in a row

<img src="https://github.com/Malek-Zaag/CTF-Writeups/blob/main/Securinets%20MiniCTF%202k22/foren/5%20in%20a%20row/1_L4TvlSS56J_Qpqyd_wFkIA.png">

The challenge was given as a 150x150 png file and as the description mentioned it was about png color channels and specifically the alpha value of a pixel.

<img src="https://github.com/Malek-Zaag/CTF-Writeups/blob/main/Securinets%20MiniCTF%202k22/foren/4%20in%20a%20row/1_wXgoEdJu-twI8R4gFJWrkg.png">

We can read from the description that the flag was hidden in the alpha value of every pixel that its order is divisible by 5 and i == j (diagonal of the image) . But before we jump to the extracting part let’s talk about the png color channel and how the data is embeded in each pixel.Each pixel in an image is represented by the model RGBA(red,green,blue,alpha) and these pixels are presenting the image as a matrix.

So the description says that the author is hidding the flag in the diagonal pixels and he gives the formula to extract it , so i concluded with a script doing it

```python
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
```

and the flag is Securinets{AlpH4_1S_vEry_H4rD}
