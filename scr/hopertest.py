from PIL import Image

im = Image.open("../assets/hopper.ppm")
print(im.format, im.size, im.mode)

r, g, b = im.split()
im = Image.merge("RGB", (b, g, r))

# out = im.resize((128, 128))
# out = im.rotate(45) # degrees counter-clockwise

# multiply each pixel by 1.2
out = im.point(lambda i: i * 1.2)

out.show()