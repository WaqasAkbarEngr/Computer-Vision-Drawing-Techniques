import cv2

image_path = "G:\Save Files\Python Save Files\CV Drawing Techniques\images"

image = cv2.imread (image_path + '\Water Drop.jpg', 1)

image_after_line_drawn = cv2.line(image, (100, 100), (200, 100), (200, 100, 250), 5)

cv2.imshow('Line Drawn in Image', image_after_line_drawn)

cv2.waitKey(0)
cv2.destroyAllWindows