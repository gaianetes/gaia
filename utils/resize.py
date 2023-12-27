#!/Users/mitchellmurphy/.pyenv/shims/python

from PIL import Image

# read image
image = Image.open("../media/flux.png")
# resize
new_image = image.resize((800, 435))
# save image
new_image.save("../media/flux-scaled.png")
