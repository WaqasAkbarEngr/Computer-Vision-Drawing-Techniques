import cv2

image_path = "G:\Save Files\Python Save Files\CV Drawing Techniques\images"

image = cv2.imread(image_path + '\Balls Graphic.jpg')

rectangle_drawn = cv2.rectangle(image, (400, 250), (850, 450), (0, 0, 0), -1)

cv2.imshow('Filled Rectangle Drawn on Image', rectangle_drawn)

cv2.waitKey(0)
cv2.destroyAllWindows