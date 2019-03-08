from PIL import Image

foreground = Image.open(r"small.jpg")
foreground = foreground.convert('RGBA')
background = Image.open(r"big.jpg")
background = background.convert('RGBA')

bwidth, bheight = background.size[0], background.size[1]
fwidth, fheight = foreground.size[0], foreground.size[1]
x, y = int((bwidth / 2) - (fwidth / 2)), int((bheight / 2) - (fheight / 2))  # центрирование
x, y = 0, 0  # в левый верхний
x, y = 0, bheight - fheight  # в левый нижний
x, y = bwidth - fwidth, bheight - fheight  # в правый нижний
x, y = bwidth - fwidth, 0  # в правый верхний

background.paste(foreground, (0, 0), mask=foreground)
background.show()
