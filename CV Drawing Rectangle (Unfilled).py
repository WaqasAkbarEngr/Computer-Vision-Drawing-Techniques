import cv2

image_path = 'G:\Save Files\Python Save Files\CV Drawing Techniques\images'

image = cv2.imread (image_path + '\Balls Graphic.jpg')

rectangle_drawn = cv2.rectangle(image, (100,100), (600,400), (0, 0, 0), 3)

cv2.imshow('Rectangle Drawn on Image', rectangle_drawn)

cv2.waitKey(0)
cv2.destroyAllWindows