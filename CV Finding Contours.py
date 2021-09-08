import cv2

image_path = "G:\Save Files\Python Save Files\CV Drawing Techniques\images"

image = cv2.imread(image_path + "\Image4Contour.jpg", 0)

edged_image = cv2.Canny(image, 50, 250)

contours, hierarchy = cv2.findContours(edged_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.imshow('Edge Detection Image after Contouring', edged_image)

print("Total Number of Contours" + str(len(contours)))

cv2.waitKey(0)
cv2.destroyAllWindows