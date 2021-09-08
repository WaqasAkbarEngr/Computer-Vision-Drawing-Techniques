import cv2

image_path = "G:\Save Files\Python Save Files\CV Drawing Techniques\images"

image = cv2.imread(image_path + '\Hawker Jet.jpg')

(rows, columns) = image.shape[:2]

ellipsed_image = cv2.ellipse(image, (int(columns/2), int(rows/2)), (450,200), 0, 0, 360, (0, 0, 0), 3)

cv2.imshow('Ellipsed Drawn on Image', ellipsed_image)

cv2.waitKey(0)
cv2.destroyAllWindows