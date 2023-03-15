import cv2

src = None
dst1, dst2, dst3 = None,None,None 

src = cv2.imread("c:/imgs/picture01.jpg")

cv2.imshow('Src',src)

cv2.waitKey(0)
cv2.destroyAllWindows