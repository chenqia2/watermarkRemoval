import numpy as np

from skimage.io import imread, imsave
from skimage.transform import resize
#from skimage.viewer import ImageViewer

img_name = '0048'
small = imread(img_name + ' (1).jpg')
big = imread(img_name+'.jpg')
logo = imread('logo.jpg', as_grey=True)

logo_resized = resize(logo, (logo.shape[0]//2, logo.shape[1]//2), mode='reflect')
small_resized = resize(small, (big.shape[0], big.shape[1]), mode='reflect')

small_resized = small_resized * 255
threshold = 0.9999
logo_bi = logo_resized<threshold

tmp = np.zeros([big.shape[0],big.shape[1],3],dtype=np.uint8)
mask = tmp>0 

startX = 130
startY = 28

stepX = 146 
stepY = 196  
for x in range(-1, 4):
    for y in range (0, 2):
        newX = startX + x*stepX
        newY = startY + y*stepY
        for i in  range(0,logo_bi.shape[0]):
            for j in  range(0,logo_bi.shape[1]):
                if newX+i>=0 and newX+i<big.shape[0] and newY+j>=0 and newY+j<big.shape[1]:
                    mask[newX+i,newY+j] = logo_bi[i,j]
                    
startX = startX+stepX//2
startY = startY+stepY//2

for x in range(-1, 4):
    for y in range (-1, 2):
        newX = startX + x*stepX
        newY = startY + y*stepY
        for i in  range(0,logo_bi.shape[0]):
            for j in  range(0,logo_bi.shape[1]):
                if newX+i>=0 and newX+i<big.shape[0] and newY+j>=0 and newY+j<big.shape[1]:
                    mask[newX+i,newY+j] = logo_bi[i,j]
result = big
for i in  range(0,big.shape[0]):
    for j in  range(0,big.shape[1]):
        if mask[i,j].all():
            result[i,j] = small_resized[i,j]
imsave(img_name+'result.jpg',result)

#viewer = ImageViewer(result)
#viewer.show()
