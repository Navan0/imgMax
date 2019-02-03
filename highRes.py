from google.colab import files
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img = np.array(Image.open('/content/mine.jpg'))
img.setflags(write=1)
img2 = np.asarray(Image.open('/content/test2.png'))
img2.setflags(write=1)
facearr = img[0:1, 0:1]
face = Image.fromarray(facearr)
plt.imshow(face)
plt.show()
shape = img.shape
h = shape[0]*4
w = shape[1]*4
c=np.zeros([h,w,3],dtype=np.uint8)
for i in 
c[0:4,0:4] = facearr
c = Image.fromarray(c)
print(facearr)
print(facearr.shape)
plt.imshow(c)
plt.show()
outimg = c.save('out.jpg')
files.download('out.jpg')
