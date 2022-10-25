import cv2

image = cv2.imread("images.png")


cv2.line(image, (255, 255), (0, 0), (0, 0, 255), 5)
cv2.arrowedLine(image, (0, 255), (1000, 255), (255, 1, 1), 5)

cv2.circle(image, (255, 255), (20), (0, 0, 0), 5)

cv2.rectangle(image, (300, 300), (0, 0), (254, 0, 0), 2)
text = "SELEBEW"
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(image, text, (500, 300), font, 1, (0, 255, 255))
cv2.imshow("frame", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
