from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img = np.array(Image.open('/content/mine.jpg')) # image to numpy array
img.setflags(write=1) # change read-only to write
img2 = np.asarray(Image.open('/content/test2.png'))
img2.setflags(write=1)
arr = Image.fromarray(img)
face = img[0:1, 0:1]
print(face)
arr2img = Image.fromarray(face2m)
plt.imshow(arr2img)
plt.show()
arr2img.save('save.jpg')
