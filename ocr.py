import cv2
import pytesseract

img = cv2.imread("data/7.png");
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

at = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)


config = "--psm 3"
text = pytesseract.image_to_string(at, config=config, lang="code")

print(text)

cv2.imshow("Img", at)
cv2.waitKey(0)
