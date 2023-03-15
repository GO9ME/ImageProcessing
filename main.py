import cv2

src = None
dst1, dst2, dst3 = None,None,None 

src = cv2.imread("c:/imgs/picture01.jpg")

dst1 = cv2.grayScale(src)
dst2 = cv2.cannyEdge(src)


cv2.imshow('Src',src)
cv2.imshow('dts1',dst1)
cv2.imshow('dts2',dst2)


cv2.waitKey(0)
cv2.destroyAllWindows