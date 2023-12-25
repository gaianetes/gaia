#!/Users/mitchellmurphy/.pyenv/shims/python

from PIL import Image

# read image
image = Image.open("../media/gaia_kubula.png")
# resize
new_image = image.resize((200, 200))
# save image
new_image.save("../media/gaianetes.png")
