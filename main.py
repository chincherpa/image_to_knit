import os
import random
from PIL import Image

file_list = []
for i in os.listdir("."):
    if i.endswith(".jpg") or i.endswith(".png"):
        file_list.append(i)

n = 38
if len(file_list) > 1:
    print("Folgende Dateien gefunden:")
    for i, fname in enumerate(file_list):
        print(f"{i}\t{fname}")
    a = input("Auswahl: ")
    IMAGE = file_list[int(a)]

CONST = 32
SIZE = 9

filename = IMAGE.split(".")[0]
result_image = f"{filename}_{CONST}_{SIZE}.jpg"
img = Image.open(IMAGE)
rgb_im = img.convert("RGB")
width, height = rgb_im.size

# image auf eine durch SIZE teilbare Größe schneiden
rgb_im.crop((0, 0, width // SIZE, height // SIZE))

for x in range(0, width, SIZE):
    for y in range(0, height, SIZE):
        r, g, b = rgb_im.getpixel((x + 3, y + 3))

        new_r = (r // CONST) * CONST
        new_g = (g // CONST) * CONST
        new_b = (b // CONST) * CONST

        knot = Image.new("RGB", (9, 9), (11, 17, 65))

        knot.putpixel((0, 2), (new_r, new_g, new_b))
        knot.putpixel((1, 1), (new_r, new_g, new_b))
        knot.putpixel((1, 2), (new_r, new_g, new_b))
        knot.putpixel((1, 3), (new_r, new_g, new_b))
        knot.putpixel((1, 4), (new_r, new_g, new_b))
        knot.putpixel((2, 2), (new_r, new_g, new_b))
        knot.putpixel((2, 3), (new_r, new_g, new_b))
        knot.putpixel((2, 4), (new_r, new_g, new_b))
        knot.putpixel((2, 5), (new_r, new_g, new_b))
        knot.putpixel((2, 6), (new_r, new_g, new_b))
        knot.putpixel((3, 3), (new_r, new_g, new_b))
        knot.putpixel((3, 4), (new_r, new_g, new_b))
        knot.putpixel((3, 5), (new_r, new_g, new_b))
        knot.putpixel((3, 6), (new_r, new_g, new_b))
        knot.putpixel((3, 7), (new_r, new_g, new_b))
        knot.putpixel((3, 8), (new_r, new_g, new_b))
        knot.putpixel((4, 4), (new_r, new_g, new_b))
        knot.putpixel((4, 5), (new_r, new_g, new_b))
        knot.putpixel((4, 6), (new_r, new_g, new_b))
        knot.putpixel((4, 7), (new_r, new_g, new_b))
        knot.putpixel((4, 8), (new_r, new_g, new_b))
        knot.putpixel((5, 3), (new_r, new_g, new_b))
        knot.putpixel((5, 4), (new_r, new_g, new_b))
        knot.putpixel((5, 5), (new_r, new_g, new_b))
        knot.putpixel((5, 6), (new_r, new_g, new_b))
        knot.putpixel((5, 7), (new_r, new_g, new_b))
        knot.putpixel((5, 8), (new_r, new_g, new_b))
        knot.putpixel((6, 2), (new_r, new_g, new_b))
        knot.putpixel((6, 3), (new_r, new_g, new_b))
        knot.putpixel((6, 4), (new_r, new_g, new_b))
        knot.putpixel((6, 5), (new_r, new_g, new_b))
        knot.putpixel((6, 6), (new_r, new_g, new_b))
        knot.putpixel((7, 1), (new_r, new_g, new_b))
        knot.putpixel((7, 2), (new_r, new_g, new_b))
        knot.putpixel((7, 3), (new_r, new_g, new_b))
        knot.putpixel((7, 4), (new_r, new_g, new_b))
        knot.putpixel((8, 2), (new_r, new_g, new_b))

        rgb_im.paste(knot, (x, y))

    if 0:
        if 0:
            new_r = (r // CONST) * CONST
            new_g = (g // CONST) * CONST
            new_b = (b // CONST) * CONST
        if 0:
            if max(r, g, b) == r:
                new_r, new_g, new_b = (r, 0, 0)
            elif max(r, g, b) == g:
                new_r, new_g, new_b = (0, g, 0)
            elif max(r, g, b) == b:
                new_r, new_g, new_b = (0, 0, b)
        if 0:
            if max(r, g, b) == r:
                new_r, new_g, new_b = (255, 0, 0)
            elif max(r, g, b) == g:
                new_r, new_g, new_b = (0, 255, 0)
            elif max(r, g, b) == b:
                new_r, new_g, new_b = (0, 0, 255)
        if 0:
            if max(r, g, b) == r:
                new_r, new_g, new_b = (random.randint(0, 255), g, b)
            elif max(r, g, b) == g:
                new_r, new_g, new_b = (r, random.randint(0, 255), b)
            elif max(r, g, b) == b:
                new_r, new_g, new_b = (r, g, random.randint(0, 255))
        if 0:
            if max(r, g, b) == r:
                new_r, new_g, new_b = (0, g, b)
            elif max(r, g, b) == g:
                new_r, new_g, new_b = (r, 0, b)
            elif max(r, g, b) == b:
                new_r, new_g, new_b = (r, g, 0)
        if 0:
            new_r, new_g, new_b = (b, r, g)
        if 0:
            new_r, new_g, new_b = (r, g, b)

        for i in range(SIZE):
            for j in range(SIZE):
                rgb_im.putpixel((x + i, y + j), (new_r, new_g, new_b))

rgb_im.save(result_image)
os.startfile(result_image)
