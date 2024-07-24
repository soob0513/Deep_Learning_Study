# 실습
import cv2

image = cv2.imread('images/01_lenna.png')
cv2.imshow('Lenna', image)
cv2.waitKey(0)
cv2.destroyAllWindows()