from PIL import Image
import numpy as np
img = np.asarray(Image.open('/home/navaneeth/work/test/mine.jpg'))
img.setflags(write=1)
img2 = np.asarray(Image.open('/home/navaneeth/work/test/test2.png'))
img2.setflags(write=1)
img2[1,0] = img[1,0]
arr = Image.fromarray(img2)
arr.save('save.jpg')
