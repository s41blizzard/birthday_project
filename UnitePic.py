from PIL import Image
from io import BytesIO
import io
import random


# Наложение фото сотрудника на фон открытки

def picture_overlay(photo):
    buf = BytesIO(photo)
    foreground = Image.open(buf)
    foreground = foreground.convert('RGBA')

    background = Image.open(r"big.jpg")
    background = background.convert('RGBA')

    bwidth, bheight = background.size[0], background.size[1]
    fwidth, fheight = foreground.size[0], foreground.size[1]
    x, y = int((bwidth / 2) - (fwidth / 2)), int((bheight / 2) - (fheight / 2))  # центрирование

    background.paste(foreground, (x, y), mask=foreground)
    img_bytes = io.BytesIO()
    background.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()


    return img_bytes
