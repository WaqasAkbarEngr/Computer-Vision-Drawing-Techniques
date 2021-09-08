import cv2

image_path = "G:\Save Files\Python Save Files\CV Drawing Techniques\images"

image = cv2.imread(image_path + '\Balls Graphic.jpg')

put_text = cv2.putText(image, "Three Balls", (500, 250), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

cv2.imshow('Text on Image', put_text)

cv2.waitKey(0)
cv2.destroyAllWindows