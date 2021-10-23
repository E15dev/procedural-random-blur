from PIL import Image
import random

i = 9

img = Image.new('RGB', (2 ** i, 2 ** i))
pixels = img.load()  # create the pixel map

for i in range(img.size[0]):  # for every pixel:
    for j in range(img.size[1]):
        print(i, j)
        pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

img.save('../out/random.png')
