import cv2

image_path = "G:\Save Files\Python Save Files\CV Drawing Techniques\images"

image = cv2.imread(image_path + '\Balls Graphic.jpg', 0)

edged_image = cv2.Canny(image, 30, 250)

contours, hierarchy = cv2.findContours(edged_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

contours_drawn = cv2.drawContours(image, contours, -1, (0, 0, 0), 5)

cv2.imshow('Contours Drawn on Image', contours_drawn)

cv2.waitKey(0)
cv2.destroyAllWindows