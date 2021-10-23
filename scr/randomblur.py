from PIL import Image
import random
from math import floor

r = []
g = []
b = []

blurradius = 4
i = 9

def sumbuf(d, i, j,br):
    x = 0
    for k in range(br):
        for l in range(br):
            x += d[i + k][j + l]
    return x

img = Image.new('RGB', (2 ** i, 2 ** i))
pixels = img.load()  # create the pixel map

for i in range(img.size[0] + blurradius):
    r.append([])
    g.append([])
    b.append([])
    for j in range(img.size[1] + blurradius):
        r[i].append(random.randint(0, 255))
        g[i].append(random.randint(0, 255))
        b[i].append(random.randint(0, 255))


for i in range(img.size[0]):  # for every pixel:
    for j in range(img.size[1]):
        print(i, j)
        rdata = floor(sumbuf(r, i, j, blurradius) / (blurradius ** 2))
        gdata = floor(sumbuf(g, i, j, blurradius) / (blurradius ** 2))
        bdata = floor(sumbuf(b, i, j, blurradius) / (blurradius ** 2))
        pixels[i, j] = (rdata, gdata, bdata)

img.save('../out/randomblur.png')
