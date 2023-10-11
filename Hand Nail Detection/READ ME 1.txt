1. Python Libraries

cv2: it is the openCV library for image processing.
numpy: it is used for numerical and array operations.
cv2_imshow: it is used to display image in google colab.

2. Properties

cv2_imread: it is used to read the path of the image and stores it in the 'image' variabe.

cv2.cvtColor(): Convert 'image' to grayscale. Grayscale images are single channel images where each pixel represents the intensity of light.

cv2.GaussianBlur(): it is used to reduce the noise.
(11,11)-Kernel size
'0' - standard deviation

cv2.adaptiveThreshold(): Adaptive threshold is used to create a binary image from the blurred image. So we use cv2.adaptiveThreshold() this function.
the resulting binary image is stored in 'threshold' variable.

cv2.findContours(): used to find contours in the binary image formed.
cv2.RETR_EXTERNAL: retrieves only the external contours.
cv2.CHAIN_APPROX_SIMPLE: simplify the contours.

nail_regions: an empty list and iterates through the contours. If the area of a contour falls within a range of 50 to 500 pixels, it is considered as a nail region, and the contour is added to the nail_regions list.

block_color: set as red in BGR format.
block_height: 20 pixels

cv2.boundingRect(): calculates the bounding rectangle around the nail region. 
(x,y)-position
(w,h)-dimension
block_y - adjust the position to place the coloured block just above the nail.
cv2.rectangle(): draws a red rectangle with the specified 'block_color' over the nail region.

