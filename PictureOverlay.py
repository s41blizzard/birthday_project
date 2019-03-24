from PIL import Image
from io import BytesIO
import io
import os, random


# Наложение фото сотрудника на фон открытки

def picture_overlay(photo, gender):
    buf = BytesIO(photo)
    foreground = Image.open(buf)
    foreground = foreground.resize((200, 260))
    foreground = foreground.convert('RGBA')
    foreground = foreground.rotate(5, expand=True)
    male_background_path = r"C:\Users\s41bl\PycharmProjects\project_birthday\male_background"
    female_background_path = r"C:\Users\s41bl\PycharmProjects\project_birthday\female_background"
    if gender == 'Женский':
        background_path = female_background_path
    else:
        background_path = male_background_path
    background_filename = random.choice(os.listdir(background_path))
    background = Image.open(background_path + "\\" + background_filename)
    background = background.convert('RGBA')

    bwidth, bheight = background.size[0], background.size[1]
    fwidth, fheight = foreground.size[0], foreground.size[1]
    x, y = int((bwidth / 2) - (fwidth / 2)), int((bheight / 2) - (fheight / 2))  # центрирование

    background.paste(foreground, (250, 250), mask=foreground)
    img_bytes = io.BytesIO()
    # background.show()
    background.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()

    return img_bytes
