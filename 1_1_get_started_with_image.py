import cv2 as cv
import sys

img = cv.imread("data/lena.jpg", 1)

if img is None:
    sys.exit("Could not read the image.")

print(img)
# cv.imshow("Display window", img)

# k = cv.waitKey(0)
# if k == ord("s"):
    # cv.imwrite("starry_night.png", img)