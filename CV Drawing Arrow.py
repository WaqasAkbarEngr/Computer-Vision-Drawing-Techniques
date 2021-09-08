import cv2

image_path = 'G:\Save Files\Python Save Files\CV Drawing Techniques\images'

image = cv2.imread(image_path + '\Balls Graphic.jpg')

arrowed_image = cv2.arrowedLine(image, (150, 200), (900, 250), (0, 0, 0), 3, tipLength= 0.05)

cv2.imshow('Arrow Drawn on Image', arrowed_image)

cv2.waitKey(0)
cv2.destroyAllWindows