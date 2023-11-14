import numpy as np
import skimage as ski

image = ski.io.imread('07.png', as_gray=False)
print(image.shape)
croppedImage = image[43:52,:]
print(croppedImage.shape)

fragment = croppedImage[0, :]   # Slice 1st row
print(fragment)
fragment2 = croppedImage[:, 0]  # Slice 1st column
print(fragment2)

# Let's check if there's any additional information in the first dimension
isAdditionalInfo = False
for i in range(1, croppedImage.shape[0]):
    if np.array_equal(fragment, croppedImage[i, :]):
        isAdditionalInfo = True
        break
print("There is additional info in the row dimension (1st dim): ", isAdditionalInfo)

# There's not, so we can reduce the dimensionality of the problem -> fragment has all the info
print(fragment)

# Let's check if the intensity of the pixels is relevant
minimum = fragment[:,3].min()
print(minimum)
print("Intensity is not relevant")

# Let's then reduce the dimensionality (629 x 3)
newFragment = fragment[:,0:3]
print(newFragment.shape)
print(newFragment[500:,:])

# There seems to be a lot of redundancy - let's reduce each vector to a single value
message = newFragment[:,0]  # Slice 1st column
print("Message:")
print(message)

# There seems also to be some periodicity - let's sample every 7th value
message = message[::7]

# Convert into characters
characterizer = lambda t: chr(t)
decodedMessage = np.array([characterizer(x) for x in message])
decodedMessage = "".join(decodedMessage)
print("Decoded message:")
print(decodedMessage)

# # There's still redundancy - let's keep only one instance of each repeating value
# singleMessage = ""
# lastCharacter = ""
# for character in decodedMessage:
#     if character != lastCharacter:
#         singleMessage += character
#         lastCharacter = character
#
# print("Single message:")
# print(singleMessage)

# The message is "smart guy, you made it. the next level is  [105, 110, 116, 101, 103, 114, 105, 116, 121]"
nextLevel = np.array([105, 110, 116, 101, 103, 114, 105, 116, 121])
decodedNextLevel = "".join(map(characterizer, nextLevel))    # Better than decodedNextLevel = np.array([characterizer(x) for x in nextLevel])
print("Decoded next level:")
print(decodedNextLevel)

# The decoded next level is -> Integrity
# Next level is http://www.pythonchallenge.com/pc/def/integrity.html








# image = ski.data.coins()
# ... or any other NumPy array!
# edges = ski.filters.sobel(image)
ski.io.imshow(newFragment)
ski.io.show()







# from PIL import Image
# import numpy as np
# from skimage import data
# import matplotlib.pyplot as plt
# # %matplotlib inline
#
#
# image = np.array(Image.open('07.png'))
# type(image)
#
# image.shape
# mask = image < 87
# image[mask]=255
# plt.imshow(image, cmap='gray')

