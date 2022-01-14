import cv2
import matplotlib.pyplot as plt

im = cv2.imread("toko.jpeg")
im_clr = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
size = im_clr.shape
new_im = im_clr[:size[0] //2, : size[1]//2]
print(new_im.shape)
plt.imshow(new_im)
plt.show()