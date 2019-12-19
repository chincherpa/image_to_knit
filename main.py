import os
from PIL import Image

IMAGE = 'image.jpg'
CONST = 64
SIZE = 5
filename = IMAGE.split('.')[0]

result_image = f'{filename}_{CONST}_{SIZE}.jpg'
img = Image.open('image.jpg')
rgb_im = img.convert('RGB')
width, height = rgb_im.size

for x in range(0, width, SIZE):
    for y in range(0, height, SIZE):
        r, g, b = rgb_im.getpixel((x, y))
        new_r = (r // CONST) * CONST
        new_g = (g // CONST) * CONST
        new_b = (b // CONST) * CONST
        for i in range(SIZE):
            for j in range(SIZE):
                rgb_im.putpixel((x + i, y + j), (new_r, new_g, new_b))

rgb_im.save(result_image)
os.startfile(result_image)
