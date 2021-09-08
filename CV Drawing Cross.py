import cv2

image_path = 'G:\Save Files\Python Save Files\CV Drawing Techniques\images'

image = cv2.imread(image_path + "\Water Drop.jpg", 1)

rows, columns = image.shape[:2]

crossed_image = cv2.line(image, (0, 0), (columns, rows), (0, 0, 0), 5)
crossed_image = cv2.line(image, (0, rows), (columns, 0), (0, 0, 0), 5)

cv2.imshow('Crossed Image', crossed_image)

cv2.waitKey(0)
cv2.destroyAllWindows