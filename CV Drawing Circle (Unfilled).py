import cv2

image_path = 'G:\Save Files\Python Save Files\CV Drawing Techniques\images'

image = cv2.imread( image_path + '\Balls Graphic.jpg')

(rows, columns) = image.shape[:2]

circle_drawn_image = cv2.circle(image, (int(columns/2),int(rows/2)), 150, (0, 0, 0), 3)

cv2.imshow('Circle Drawn on Image', circle_drawn_image)

cv2.waitKey(0)
cv2.destroyAllWindows