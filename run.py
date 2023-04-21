from PIL import Image
import numpy as np

def image_to_ascii(image_path, width=800, height=800):
    image = Image.open(image_path)
    image = image.resize((width, height))
    pixels = np.asarray(image)
    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"
    chars = chars[::-1]
    new_image = []
    for row in pixels:
        new_row = ""
        for pixel in row:
            new_row += chars[int(np.average(pixel)) // 4]
        new_image.append(new_row)
    return "\n".join(new_image)

print(image_to_ascii("/mnt/f/git/Image-to-ascii-art-generator-Python-/AC.jpg"))
