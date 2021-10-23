from PIL import Image
import random
from math import floor

buf = []

blurradius = 4
i = 9

def sumbuf(i, j,br):
    global buf
    x = 0
    for k in range(br):
        for l in range(br):
            x += buf[i + k][j + l]
    return x

img = Image.new('RGB', (2 ** i, 2 ** i))
pixels = img.load()  # create the pixel map

for i in range(img.size[0] + blurradius):
    buf.append([])
    for j in range(img.size[1] + blurradius):
        buf[i].append(random.randint(0, 255))


for i in range(img.size[0]):  # for every pixel:
    for j in range(img.size[1]):
        print(i, j)
        data = floor(sumbuf(i, j, blurradius) / (blurradius ** 2))
        # data = floor((buf[i][j] + buf[i][j + 1] + buf[i + 1][j] + buf[i + 1][j + 1]) / 4)
        pixels[i, j] = (0, 0, data)

img.save('../out/randomblueblur.png')
