import cv2

image_path = "G:\Save Files\Python Save Files\CV Drawing Techniques\images"

image = cv2.imread(image_path + '\Lightning.jpg')

(rows, columns) = image.shape[:2]

filled_circled_image = cv2.circle(image, (int(columns/2),int(rows/2)), 250, (0, 0, 0), -1)

cv2.imshow('Filled Circle Drawn on Image', filled_circled_image)

cv2.waitKey(0)
cv2.destroyAllWindows