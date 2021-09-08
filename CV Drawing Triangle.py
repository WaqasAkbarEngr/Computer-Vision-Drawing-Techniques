import cv2

image_path = "G:\Save Files\Python Save Files\CV Drawing Techniques\images"

image = cv2.imread(image_path + '\Balls Graphic.jpg')

triangled_image = cv2.line(image, (50, 50), (50, 150), (0, 0, 0), 3)
cv2.line(triangled_image, (50,150), (300, 150), (0, 0, 0), 3)
cv2.line(triangled_image, (300, 150), (50, 50), (0, 0, 0), 3)

cv2.imshow('Triangle on Image', triangled_image)

cv2.waitKey(0)
cv2.destroyAllWindows