import numpy as np
import skimage as ski

image = ski.io.imread('11.jpg', as_gray=False)
print(image.shape)
print(image[0,0:10,:])
print(image[0:10,0,:])

width = image.shape[1]
height = image.shape[0]

# It's two interlaced images - let's decouple them

image1 = image[0::2,:,:]
image1 = image1[:,0::2,:]
print("********************")
print(image1[0,0:10,:])
ski.io.imshow(image1)
ski.io.show()

# And the answer is: evil
# http://www.pythonchallenge.com/pc/def/evil.html


